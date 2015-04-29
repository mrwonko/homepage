import flask
import werkzeug.exceptions
import bleach
import tidylib

import local_config

def _fail():
    raise werkzeug.exceptions.BadRequest( "Malformed data!" )

class Sanitizer:
    @staticmethod
    def ancestor_of( obj ):
        return issubclass( obj.__class__, Sanitizer )
    
    def sanitize( self, input ):
        raise Exception( "Not implemented!" )

class List( Sanitizer ):
    def __init__( self, content ):
        assert Sanitizer.ancestor_of( content )
        self.content = content
    
    def sanitize( self, l ):
        if type( l ) != list:
            _fail()
        result = []
        for item in l:
            result.append( self.content.sanitize( item ) )
        return result

class Optional:
    def __init__( self, content ):
        assert Sanitizer.ancestor_of( content )
        self.content = content

class Object( Sanitizer ):
    def __init__( self, **args ):
        assert all( [
            type( key ) in ( str, unicode )
            and ( Sanitizer.ancestor_of( value ) or value.__class__ == Optional )
            for key, value in args.items()
        ] )
        self.items = args
    
    def sanitize( self, d ):
        if type( d ) != dict:
            _fail()
        result = {}
        for key, expected in self.items.items():
            if expected.__class__ == Optional:
                if key not in d or d[ key ] == None:
                    result[ key ] = None
                    continue
                expected = expected.content
            if key not in d:
                _fail()
            result[ key ] = expected.sanitize( d[ key ] )
        return result

class _Text( Sanitizer ):
    def sanitize( self, text ):
        if type( text ) not in ( str, unicode ):
            _fail()
        return text
Text = _Text()

def clean( html ):
    if not html:
        return html
    clean = bleach.clean( html, tags = local_config.TAG_WHITELIST, attributes = local_config.ATTRIBUTE_WHITELIST )
    # catches some additional problems
    tidy, warnings = tidylib.tidy_fragment( clean )
    return tidy

def escape( html ):
    if not html:
        return html
    return flask.escape( html )
