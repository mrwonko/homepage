import klein
import json

import just_mail
import just_akismet
import just_database
import just_sanitize
import local_config

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

_comment_admin_template = just_sanitize.Object(
    action = just_sanitize.Text
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

app = klein.Klein()

def to_json( data, request = None ):
    if request:
        request.setHeader( "content-type", "application/json" )
    return json.dumps( data, check_circular = False )

@app.route( "/rest/blog/<int:year>/<slug>/comments", methods = [ 'GET' ] )
def get_comments( request, year, slug ):
    post = "/".join( [ str( year ), slug ] )
    return just_database.get_comments( post )\
        .addCallback( to_json, request )

app.run( local_config.HOST, local_config.PORT )

"""
_app = flask.Flask( __name__ )

_app.secret_key = local_config.SESSION_KEY

@_app.route( "/rest/blog/<year>/<slug>/comments", methods = [ 'GET' ] )
def get_comments( year, slug ):
    post = "/".join( ( year, slug ) )
    return flask.json.jsonify( comments = just_database.get_comments( post ) )

@_app.route( "/rest/blog/<year>/<slug>/comments", methods = [ 'POST' ] )
def post_comment( year, slug ):
    post = "/".join( ( year, slug ) )
    
    comment = _comment_template.sanitize( flask.request.get_json() )
    comment[ "user_agent" ] = flask.request.headers.get( "User-Agent" )
    comment[ "referrer" ] = flask.request.environ.get( "HTTP_REFERER", None )
    comment[ "ip" ] = flask.request.remote_addr # environ[ "REMOTE_ADDR" ]
    
    spammy = just_akismet.check( _comment_to_akismet( comment ) ) if local_config.AKISMET_ENABLED else "HAM"
    if spammy == "DISCARD":
        return flask.json.jsonify( spam = True )
    # make the html in the comment body nice and safe
    comment[ "content" ] = just_sanitize.clean( comment[ "content" ] )
    
    id = just_database.new_comment( post, comment, spammy == "SPAM" )
    
    _logger.info( "New comment by {author}, it's {spammy}.".format( author = comment[ "author" ], spammy = spammy ) )    
    escaped_comment = { key: just_sanitize.escape( value ) for key, value in comment.items() }
    escaped_comment[ "id" ] = id
    escaped_comment[ "post" ] = post
    just_mail.send( "New Blog Comment", local_config.MAIL_BODY_NEW_COMMENT.format( comment = escaped_comment, spammy = spammy ) )
    return flask.json.jsonify( spam = False )

@_app.route( "/rest/downloads/<path:filename>", methods = [ 'GET' ] )
def get_downloads( filename ):
    return flask.json.jsonify( downloads = just_database.get_download_count( filename ) + local_config.LEGACY_DOWNLOADS.get( filename, 0 ) )

@_app.route( "/internal/rest/downloads/<path:filename>", methods = [ 'POST' ] )
def on_download( filename ):
    just_database.new_download( filename )
    return flask.json.jsonify( success = True )

@_app.route( "/admin/rest/blog/comments/unapproved", methods = [ 'GET' ] )
def get_unapproved_comments():
    return flask.json.jsonify( comments = just_database.get_unapproved_comments() )

@_app.route( "/admin/rest/blog/comments/<id>", methods = [ 'POST' ] )
def admin_comment( id ):
    body = _comment_admin_template.sanitize( flask.request.get_json() )
    action = body[ "action" ]
    if action not in ( "delete", "spam", "approve" ):
        raise werkzeug.exceptions.BadRequest( "Invalid action!" )
    
    if action == "delete":
        return flask.json.jsonify( success = just_database.trash_comment( id ) )
    
    # retrieve comment (so we can send it to Akismet) and delete/approve it
    # use a transaction so it's atomic (deletion then shouldn't ever fail)
    with just_database.new_transaction() as transaction:
        comment = just_database.get_comment( transaction, id )
        if not Comment:
            return flask.json.jsonify( success = False, error = "No such comment!" )
        if action == "spam":
            success = just_database.trash_comment( transaction, id )
        else:
            assert( action == "approve" )
            success = just_database.approve_comment( transaction, id )
        assert success
    # spamming an undetected comment
    if action == "spam" and not comment[ "spam" ] and local_config.AKISMET_ENABLED:
        just_akismet.spam( _comment_to_akismet( comment ) )
    # approving a detected comment implies hamming it
    if action == "approve" and comment[ "spam" ] and local_config.AKISMET_ENABLED:
        just_akismet.ham( _comment_to_akismet( comment ) )
    return flask.json.jsonify( success = True )

if __name__ == "__main__":
    _app.run( host = local_config.HOST, port = local_config.PORT )
"""
