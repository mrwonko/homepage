import flask
import logging
import werkzeug.exceptions

import just_mail
import just_akismet
import just_database
import just_sanitize
import local_config

logging.basicConfig()

_logger = logging.Logger( __name__ )
_logger.addHandler( logging.StreamHandler() ) # output to stdout/stderr

_akismet_defaults_comment = {
    "blog": "http://mrwonko.de/blog",
    "blog_lang": "en",
    "blog_charset": "UTF-8",
    "comment_type": "comment"
}

_akismet_defaults_contact = {
    "blog": "http://mrwonko.de/contact", # TODO
    "blog_charset": "UTF-8",
    "blog_lang": "en, de",
    "comment_type": "contact-form"
}

_comment_template = just_sanitize.Object(
    author = just_sanitize.Text,
    email = just_sanitize.Text,
    url = just_sanitize.Optional( just_sanitize.Text ),
    content = just_sanitize.Text
)

_comment_to_akismet_LUT = {
    "author": "comment_author",
    "email": "comment_author_email",
    "content": "comment_content",
    "url": "comment_author_url",

    "user_agent": "user_agent",
    "referrer": "referrer",
    "ip": "user_ip"
}

def _comment_to_akismet( comment ):
    akismet = _akismet_defaults_comment.copy()
    for src, dst in _comment_to_akismet_LUT.items():
        akismet[ dst ] = comment[ src ]
    return akismet

#just_mail.send( "another test", "test 123" )
#just_akismet.check( test_data )

_app = flask.Flask( __name__ )

_app.secret_key = local_config.SESSION_KEY

@_app.route( "/rest/blog/<year>/<slug>/comments", methods = [ 'GET' ] )
def get_comments( year, slug ):
    post = "/".join( ( year, slug ) )
    return flask.json.jsonify( comments = just_database.get_comments( post ) )

@_app.route( "/rest/blog/<year>/<slug>/comments", methods = [ 'POST' ] )
def post_comment( year, slug ):
    print( flask.request.get_json() )
    comment = _comment_template.sanitize( flask.request.get_json() )
    comment[ "user_agent" ] = flask.request.headers.get( "User-Agent" )
    comment[ "referrer" ] = flask.request.environ.get( "HTTP_REFERER", None )
    comment[ "ip" ] = flask.request.remote_addr # environ[ "REMOTE_ADDR" ]
    
    spammy = just_akismet.check( _comment_to_akismet( comment ) )
    if spammy == "DISCARD":
        return flask.json.jsonify( spam = True )
    # make the html in the comment body nice and safe
    comment[ "content" ] = just_sanitize.clean( comment[ "content" ] )
    just_database.new_comment( "/".join( ( year, slug ) ), comment, spammy == "SPAM" )
    return flask.json.jsonify( spam = False )

@_app.route( "/rest/downloads/<path:filename>", methods = [ 'GET' ] )
def get_downloads( filename ):
    return flask.json.jsonify( downloads = just_database.get_download_count( filename ) + local_config.LEGACY_DOWNLOADS.get( filename, 0 ) )

@_app.route( "/internal/rest/downloads/<path:filename>", methods = [ 'POST' ] )
def on_download( filename ):
    just_database.new_download( filename )
    return flask.json.jsonify( success = True )

if __name__ == "__main__":
    _app.run( host = local_config.HOST, port = local_config.PORT )
