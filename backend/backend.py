from __future__ import print_function
import klein
import json
import sys
import werkzeug.exceptions
from twisted.internet import defer, reactor
from twisted.python import log
from twisted.web.server import Site

import just_mail
import just_akismet
import just_database
import just_sanitize
import local_config

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
    if not content_type or content_type.lower() != "application/json":
        raise werkzeug.exceptions.BadRequest( "content-type must be application/json!" )
    try:
        obj = json.loads( request.content.read() )
    except ValueError:
        raise werkzeug.exceptions.BadRequest( "invalid json!" )
    return template.sanitize( obj ) if template else obj

def _handle_cors( request ):
    if local_config.ALLOW_CROSS_ORIGIN:
        request.setHeader( 'Access-Control-Allow-Origin', '*' )
        request.setHeader( 'Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept' )

def _options( request, options ):
    request.setHeader( 'Allow', options )
    _handle_cors( request )

#    Routes

app = klein.Klein()

# options requests; adding CORS so Cross Origin Requests work
@app.route( "/rest/blog/<int:year>/<slug>/comments", methods = [ 'OPTIONS' ] )
def comments_options( request, year, slug ):
    _options( request, 'GET, HEAD, POST' )
    return ""
@app.route( "/rest/downloads/<path:filename>", methods = [ 'OPTIONS' ] )
def download_options( request, year, slug ):
    _options( request, 'GET, HEAD' )
    return ""
@app.route( "/admin/rest/blog/comments/unapproved", methods = [ 'OPTIONS' ] )
def unapproved_options( request, year, slug ):
    _options( request, 'GET, HEAD' )
    return ""
@app.route( "/admin/rest/blog/comments/<int:comment_id>", methods = [ 'OPTIONS' ] )
def admin_options( request, year, slug ):
    _options( request, 'POST' )
    return ""

# get comments for article
@app.route( "/rest/blog/<int:year>/<slug>/comments", methods = [ 'GET' ] )
@defer.inlineCallbacks
def get_comments( request, year, slug ):
    _handle_cors( request )
    post = "/".join( [ str( year ), slug ] )
    comments = yield just_database.get_comments( post )
    defer.returnValue( _to_json( { "comments": comments }, request ) )

# post comment to article
@app.route( "/rest/blog/<int:year>/<slug>/comments", methods = [ 'POST' ] )
@defer.inlineCallbacks
def post_comment( request, year, slug ):
    _handle_cors( request )
    year = str( year )
    post = "/".join( ( year, slug ) )
    
    comment = _from_json( request, _comment_template )
    comment[ "user_agent" ] = request.getHeader( "user-agent" )
    comment[ "referrer" ] = request.getHeader( "referer" )
    comment[ "ip" ] = request.getClientIP()
    
    # make the html in the comment body nice and safe
    # this might lead to a slightly worse akismet detection, but is required for spam submission to use the same content as the check.
    log.msg( comment["content"] )
    comment[ "content" ] = comment[ "content" ].replace( "\n", "<br/>" )
    comment[ "content" ] = just_sanitize.clean( comment[ "content" ] )
    log.msg( comment["content"] )
    
    # akismet check, if desired
    spammy = yield just_akismet.check( _comment_to_akismet( comment ) )
    if spammy == "DISCARD":
        # only trash if Akismet is sure, otherwise let admin decide
        defer.returnValue( _to_json( { "spam": True }, request ) )
    
    # insert comment into database
    id = yield just_database.new_comment( post, comment, spammy == "SPAM" )
    
    log.msg( "New comment by {author}, it's {spammy}.".format( author = comment[ "author" ], spammy = spammy ) )
    
    # send mail notification
    escaped_comment = { key: just_sanitize.escape( value ) for key, value in comment.items() }
    escaped_comment[ "id" ] = id
    escaped_comment[ "post" ] = post
    # not yielded, i.e. we don't wait for success/failure; we just log failure and answer the request straight away
    just_mail.send( "New Blog Comment", local_config.MAIL_BODY_NEW_COMMENT.format( comment = escaped_comment, spammy = spammy.lower() ) )\
    .addErrback( log.err )
    
    defer.returnValue( _to_json( { "spam": False }, request ) )

# get download count
@app.route( "/rest/downloads/<path:filename>", methods = [ 'GET' ] )
@defer.inlineCallbacks
def get_downloads( request, filename ):
    _handle_cors( request )
    downloads = ( yield just_database.get_download_count( filename ) ) + local_config.LEGACY_DOWNLOADS.get( filename, 0 )
    defer.returnValue( _to_json( { "downloads": downloads }, request ) )

# register a finished download (internally called by nginx, not publicly proxied)
@app.route( "/internal/onDownload", methods = [ 'GET' ] )
@defer.inlineCallbacks
def on_download( request ):
    _handle_cors( request )
    print( "{}".format( request.args ) )
    if "file" not in request.args or request.args.get( "completion", [ "" ] )[ 0 ] != "OK" or request.args.get( "method", [ "" ] )[ 0 ] != "GET":
        defer.returnValue( _to_json( { "success": False }, request ) )
    yield just_database.new_download( request.args[ "file" ][ 0 ].lstrip( "/" ) )
    defer.returnValue( _to_json( { "success": True }, request ) )

# admin: retrieve unapproved comments
@app.route( "/admin/rest/blog/comments/unapproved", methods = [ 'GET' ] )
@defer.inlineCallbacks
def get_unapproved( request ):
    _handle_cors( request )
    comments = yield just_database.get_unapproved_comments()
    defer.returnValue( _to_json( { "comments": comments }, request ) )

# admin a comment
@app.route( "/admin/rest/blog/comments/<int:comment_id>", methods = [ 'POST' ] )
@defer.inlineCallbacks
def admin_comment( request, comment_id ):
    _handle_cors( request )
    def respond( success ):
        defer.returnValue( _to_json( { "success": success }, request ) )
    body = _from_json( request, _comment_admin_template )
    action = body[ "action" ]
    if action == "delete":
        comment = yield just_database.trash_comment( comment_id )
        respond( comment != None )
    elif action == "approve":
        comment = yield just_database.approve_comment( comment_id )
        if not comment:
            respond( False )
        if comment[ "spam" ]:
            # report false positive to Akismet
            yield just_akismet.ham( _comment_to_akismet( comment ) )
        respond( True )
    elif action == "spam":
        comment = yield just_database.trash_comment( comment_id )
        if not comment:
            respond( False )
        if not comment[ "spam" ]:
            # report false negative to Akismet
            yield just_akismet.spam( _comment_to_akismet( comment ) )
        respond( True )
    else:
        raise werkzeug.exceptions.BadRequest( "Invalid action!" )

#    Entry Point

# for using twistd
resource = app.resource()

if __name__ == "__main__":
    # make twisted log to stdout/stderr
    def _stdout_stderr_observer( log ):
        print( *log[ "message" ], file = sys.stderr if log[ "isError" ] else sys.stdout )
    log.startLoggingWithObserver( _stdout_stderr_observer, setStdout = False )

    reactor.listenTCP( local_config.PORT, Site( resource ), interface = local_config.HOST )
    reactor.run()
