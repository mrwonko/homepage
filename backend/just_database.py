import sqlalchemy
import itertools
import alchimia # TODO: maybe txpostgres would be better? a threaded solution is not very nice, and alchimia is lacking some sqlalchemy features anyway?
from twisted.internet import reactor, defer
from twisted.python import log

import local_config

_address = "postgresql+psycopg2://{name}:{password}@{host}/{database}".format(
    name = local_config.DB_USER,
    password = local_config.DB_PASS,
    host = local_config.DB_HOST,
    database = local_config.DB_DB
)

_engine = sqlalchemy.create_engine( _address, reactor = reactor, strategy = alchimia.TWISTED_STRATEGY )
_sync_engine = sqlalchemy.create_engine( _address )
_sync_metadata = sqlalchemy.MetaData( _sync_engine )
_comments = sqlalchemy.Table( "comments", _sync_metadata, autoload = True )
_downloads = sqlalchemy.Table( "downloads", _sync_metadata, autoload = True )
_download_names = sqlalchemy.Table( "download_names", _sync_metadata, autoload = True )

# prebuild the statement; doing it this way prevents SQL injections.
_select_comments = sqlalchemy.\
    select( [
        _comments.c.time,
        _comments.c.author,
        _comments.c.content,
        _comments.c.url
    ] ).\
    select_from( _comments ).\
    where(
        # note the parens due to bitwise and binding less strongly than equals
        ( _comments.c.post == sqlalchemy.bindparam( "post" ) ) & ( _comments.c.approved == True )
    ).\
    order_by( _comments.c.time.asc() )

_select_download_count = sqlalchemy.\
    select( [ sqlalchemy.func.count( _downloads.c.id ) ] ).\
    select_from( _downloads.join( _download_names ) ).\
    where( _download_names.c.name == sqlalchemy.bindparam( "name" ) )

_select_download_id = sqlalchemy.\
    select( [ _download_names.c.id ] ).\
    where( _download_names.c.name == sqlalchemy.bindparam( "name" ) )

_delete_comment = sqlalchemy.\
    delete( _comments ).\
    where( _comments.c.id == sqlalchemy.bindparam( "deleted_id" ) )

_approve_comment = sqlalchemy.\
    update( _comments ).\
    where( _comments.c.id == sqlalchemy.bindparam( "approved_id" ) ).\
    values( approved = True, spam = False )

#   Public functions

@defer.inlineCallbacks
def get_comments( post ):
    """
    Returns list of comments for a specific post.
    
    Comments only contain public information and are sorted by time.
    """
    
    res = []
    response = yield _engine.execute( _select_comments, post = post )
    cols = yield response.fetchall()
    for time, author, content, url in cols:
        res.append( {
                "time":  time.isoformat(),
                "author": author,
                "content": content,
                "url": url
            } )
    defer.returnValue( res )

@defer.inlineCallbacks
def new_comment( post, data, spam = False ):
    """
    Create a new comment, using mostly the data in "data".
    """
    
    defaulted_data = {
        "url": None,
        "referrer": None
    }
    defaulted_data.update( data )
    result = yield _engine.execute( _comments.insert().values( post = post, spam = spam, approved = False, **defaulted_data ) )
    defer.returnValue( result.inserted_primary_key[ 0 ] )

@defer.inlineCallbacks
def get_download_count( name ):
    result = yield _engine.execute( _select_download_count, name = name )
    first = yield result.first()
    defer.returnValue( first[ 0 ] )

@defer.inlineCallbacks
def new_download( name ):
    log.msg( "new_download( \"{}\" )".format( name ) )
    # we need atomicity for "insert if not exist" so we use a transaction
    connection = yield _engine.connect()
    log.msg( "connection established")
    try:
        transaction = yield connection.begin()
        log.msg( "transaction started" )
        try:
            result = yield transaction.execute( _select_download_id, name = name )
            log.msg( "download name looked up" )
            if result.rowcount == 0:
                result.close()
                result = yield transaction.execute( _download_names.insert().values( name = name ) )
                log.msg( "new download name inserted" )
                key = result.inserted_primary_key[ 0 ]
                result.close()
            else:
                first = yield result.first()
                key = first[ 0 ]
        except:
            yield transaction.rollback()
            log.msg( "transaction rolled back" )
            raise
        else:
            yield transaction.commit()
            log.msg( "transaction comitted" )
        yield connection.execute( _downloads.insert().values( download = key ) )
        log.msg( "download inserted" )
    finally:
        connection.close()
        log.msg( "connection closed" )
    defer.returnValue( None )

#   Admin functions

def get_unapproved_comments():
    """
    Returns list of all unapproved comments.
    
    Unlike get_comments() this returns *all* columns since it's for administrative use.
    """
    
    result = []
    response = _engine.execute( _comments.select( _comments.c.approved == False ) )
    for row in response:
        comment = { column : value for column, value in itertools.izip( response.keys(), row ) }
        comment[ "time" ] = comment[ "time" ].isoformat()
        result.append( comment )
    response.close()
    return result

def _get_comment( transaction, id ):
    response = transaction.execute( _comments.select( _comments.c.id == id ) )
    if response.rowcount == 0:
        response.close()
        return None
    comment = { key: value for key, value in zip( response.keys(), response.first() ) }
    comment[ "time" ] = comment[ "time" ].isoformat()
    return comment

def trash_comment( transaction, id ):
    return transaction.execute( _delete_comment, deleted_id = id ).rowcount > 0

def approve_comment( transaction, id ):
    return transaction.execute( _approve_comment, approved_id = id ).rowcount > 0

