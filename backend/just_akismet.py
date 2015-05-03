import twisted
from twisted.internet import reactor, defer, ssl
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent, FileBodyProducer, ResponseDone
from twisted.web.http_headers import Headers
from twisted.python.failure import Failure
from twisted.python import log
import werkzeug.exceptions
from urllib import urlencode
from StringIO import StringIO # cStringIO may be faster?

import local_config


check_url = "http://{apikey}.rest.akismet.com/1.1/comment-check".format( apikey = local_config.AKISMET_KEY )
ham_url = "https://{apikey}.rest.akismet.com/1.1/submit-ham".format( apikey = local_config.AKISMET_KEY )
spam_url = "https://{apikey}.rest.akismet.com/1.1/submit-spam".format( apikey = local_config.AKISMET_KEY )

headers = Headers( {
    "User-Agent": [ "twisted/{version} | just_akismet/1.0.0".format( version = twisted.__version__ ) ],
    "Content-Type": [ "application/x-www-form-urlencoded" ]
} )

class WebClientContextFactory(ssl.ClientContextFactory):
    def getContext( self, hostname, port ):
        return ssl.ClientContextFactory.getContext( self )

agent = Agent( reactor ) if local_config.AKISMET_CHECK_CERTS else Agent( reactor, WebClientContextFactory() )

class BodyReceiver( Protocol ):
    def __init__( self, finished ):
        self.finished = finished
        self.received = []
    def dataReceived( self, bytes ):
        self.received.append( bytes )
    def connectionLost( self, reason ):
        if reason.check( ResponseDone ):
            # cleanly closed
            self.finished.callback( "".join( self.received ) )
        else:
            # not cleanly closed
            self.finished.errback( reason )

def _get_response_body( response ):
    finished = defer.Deferred()
    response.deliverBody( BodyReceiver( finished ) )
    return finished

@defer.inlineCallbacks
def check( data ):
    """
    Does an Akismet request with the supplied data.
    
    Returns "SPAM", "HAM" or "DISCARD" (definite spam)
    or raises BadGateway/InternalServerError on failure
    
    """
    if not local_config.AKISMET_ENABLED:
        defer.returnValue( "HAM" )
    
    body = urlencode( { key: value for key, value in data.items() if value != None }, doseq = True )
    try:
        response = yield agent.request( "POST", check_url, headers, FileBodyProducer( StringIO( body ) ) )
    except Exception as e:
        raise werkzeug.exceptions.BadGateway( "Error sending Akismet request: {}: {}".format( e.__class__.__name__, e.reasons[0].getErrorMessage() ) )
    if response.code / 100 != 2:
        raise werkzeug.exceptions.BadGateway( "Akismet sent code {}".format( response.code ) )
    try:
        response_body = yield _get_response_body( response )
    except Exception as e:
        raise werkzeug.exceptions.BadGateway( "Error receiving Akismet response body: {}".format( e ) )
    if response_body not in [ "true", "false" ]:
        hint = response.headers.getRawHeaders( "X-akismet-debug-help", [ "no details available" ] )[ 0 ]
        raise werkzeug.exceptions.InternalServerError( "Sent invalid Akismet request, got \"{}\": {}".format( response_body, hint ) )
    if response_body == "true":
        if response.headers.getRawHeaders( "X-akismet-pro-tip", [ "keep" ] )[ 0 ] == "discard":
            defer.returnValue( "DISCARD" )
        defer.returnValue( "SPAM" )
    defer.returnValue( "HAM" )

@defer.inlineCallbacks
def spam( data ):
    if not local_config.AKISMET_ENABLED:
        log.msg( "Comment by '{}' spammed but Akismet submission disabled".format( data["comment_author"] ) )
        defer.returnValue( None )
    
    body = urlencode( { key: value for key, value in data.items() if value != None }, doseq = True )
    response = yield agent.request( "POST", spam_url, headers, FileBodyProducer( StringIO( body ) ) )
    if response.code / 100 != 2:
        response_body = yield _get_response_body( response )
        raise werkzeug.exceptions.InternalServerError( "Sent invalid Akismet request, got {}: {}".format( response.code, response_body ) )
    defer.returnValue( None )

@defer.inlineCallbacks
def ham( data ):
    if not local_config.AKISMET_ENABLED:
        log.msg( "Comment by '{}' hammed but Akismet submission disabled".format( data["comment_author"] ) )
        defer.returnValue( None )
    body = urlencode( { key: value for key, value in data.items() if value != None }, doseq = True )
    response = yield agent.request( "POST", ham_url, headers, FileBodyProducer( StringIO( body ) ) )
    if response.code / 100 != 2:
        response_body = yield _get_response_body( response )
        raise werkzeug.exceptions.InternalServerError( "Sent invalid Akismet request, got {}: {}".format( response.code, response_body ) )
    defer.returnValue( None )
