import flask
from urllib import urlencode
import urllib2
import logging

import local_config

logger = logging.Logger( __name__ )
logger.addHandler( logging.StreamHandler() ) # output to stdout/stderr


check_url = "https://{apikey}.rest.akismet.com/1.1/comment-check".format( apikey = local_config.AKISMET_KEY )
ham_url = "https://{apikey}.rest.akismet.com/1.1/submit-ham".format( apikey = local_config.AKISMET_KEY )
spam_url = "https://{apikey}.rest.akismet.com/1.1/submit-spam".format( apikey = local_config.AKISMET_KEY )

headers = {
    "User-Agent": "Flask/{version} | just_akismet/1.0.0".format( version = flask.__version__ )
}

class LogicError( Exception ):
    pass

class RequestError( Exception ):
    pass

def check( data ):
    """
    Does an Akismet request with the supplied data.
    
    Returns "SPAM", "HAM" or "DISCARD" (definite spam)
    or raises a RequestError on failure to connect
    or a LogicError if data is rejected
    
    """
    request = urllib2.Request( check_url, urlencode( data, doseq = True ), headers )
    response = urllib2.urlopen( request )
    if response.code / 100 != 2:
        raise RequestError( response.msg )
    body = response.read()
    if body not in ( "true", "false" ):
        raise LogicError( "Invalid Akismet Request: {}".format( response.headers.get( "X-akismet-debug-help", "<no details available>" ) ) )
    if body == "true":
        if response.headers.get( "X-akismet-pro-tip", "keep" ) == "discard":
            return "DISCARD"
        return "SPAM"
    return "HAM"

def spam( data ):
    request = urllib2.Request( spam_url, urlencode( data, doseq = True ), headers )
    response = urllib2.urlopen( request )
    if response.code / 100 != 2:
        raise RequestError( response.msg )

def ham( data ):
    request = urllib2.Request( ham_url, urlencode( data, doseq = True ), headers )
    response = urllib2.urlopen( request )
    if response.code / 100 != 2:
        raise RequestError( response.msg )