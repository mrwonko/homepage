import klein
import json
import sys
import werkzeug.exceptions
from twisted.internet import defer
from twisted.python import log
from twisted.web.server import Site

import just_mail
import just_akismet
import just_database
import just_sanitize
import local_config

#    Logging

# make twisted log to stdout/stderr
def _stdout_stderr_observer( log ):
    print( *log[ "message" ], file = sys.stderr if log[ "isError" ] else sys.stdout )

log.startLoggingWithObserver( _stdout_stderr_observer, setStdout = False )

#    Akismet

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

#    Utility

def _to_json( data, request = None ):
    text = json.dumps( data, check_circular = False )
    if request:
        request.setHeader( "content-type", "application/json" )
        request.setHeader( "content-length", str( len( text ) ) )
        if request.method == "HEAD":
            return ""
    return text

def _get_content_type( request ):
    content_type = request.getHeader( b"content-type" )
    if not content_type:
        raise werkzeug.exceptions.BadRequest( "no content-type set!" )
    if content_type.find( ";" ) == -1:
        return content_type, []
    content_type, parameters = content_type.split( ";", 1 )
    return content_type, [ param.strip() for param in parameters.split( ";" ) ]

def _from_json( request, template = None ):
    content_type, params = _get_content_type( request )
    print( "content type: {}".format( content_type ) )
    if not content_type or content_type.lower() != "application/json":
        raise werkzeug.exceptions.BadRequest( "content-type must be application/json!" )
    try:
        obj = json.loads( request.content.read() )
    except ValueError:
        raise werkzeug.exceptions.BadRequest( "invalid json!" )
    return template.sanitize( obj ) if template else obj

#    Routes

app = klein.Klein()

@app.route( "/rest/blog/<int:year>/<slug>/comments", methods = [ 'GET' ] )
def get_comments( request, year, slug ):
    post = "/".join( [ str( year ), slug ] )
    return just_database.get_comments( post )\
        .addCallback( lambda comments: { "comments": comments } )\
        .addCallback( _to_json, request )

@app.route( "/rest/blog/<int:year>/<slug>/comments", methods = [ 'POST' ] )
@defer.inlineCallbacks
def post_comment( request, year, slug ):
    year = str( year )
    post = "/".join( ( year, slug ) )
    
    comment = _from_json( request, _comment_template )
    comment[ "user_agent" ] = request.getHeader( "user-agent" )
    comment[ "referrer" ] = request.getHeader( "referer" )
    comment[ "ip" ] = request.getClientIP()
    
    # akismet check, if desired
    spammy = ( yield just_akismet.check( _comment_to_akismet( comment ) ) ) if local_config.AKISMET_ENABLED else "HAM"
    if spammy == "DISCARD":
        # only trash if Akismet is sure, otherwise let admin decide
        defer.returnValue( _to_json( { "spam": True }, request ) )
    
    # make the html in the comment body nice and safe
    comment[ "content" ] = just_sanitize.clean( comment[ "content" ] )
    
    # insert comment into database
    id = yield just_database.new_comment( post, comment, spammy == "SPAM" )
    
    log.msg( "New comment by {author}, it's {spammy}.".format( author = comment[ "author" ], spammy = spammy ) )
    
    # send mail notification
    escaped_comment = { key: just_sanitize.escape( value ) for key, value in comment.items() }
    escaped_comment[ "id" ] = id
    escaped_comment[ "post" ] = post
    yield just_mail.send( "New Blog Comment", local_config.MAIL_BODY_NEW_COMMENT.format( comment = escaped_comment, spammy = spammy.lower() ) )
    
    defer.returnValue( _to_json( { "spam": False }, request ) )

@app.route( "/rest/downloads/<path:filename>", methods = [ 'GET' ] )
@defer.inlineCallbacks
def get_downloads( request, filename ):
    downloads = ( yield just_database.get_download_count( filename ) ) + local_config.LEGACY_DOWNLOADS.get( filename, 0 )
    defer.returnValue( _to_json( { "downloads": downloads }, request ) )

@app.route( "/internal/rest/downloads/<path:filename>", methods = [ 'POST' ] )
@defer.inlineCallbacks
def on_download( request, filename ):
    yield just_database.new_download( filename )
    defer.returnValue( _to_json( { "success": True }, request ) )

log.startLoggingWithObserver

app.run( local_config.HOST, local_config.PORT )

"""

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
