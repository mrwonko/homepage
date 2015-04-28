import sqlalchemy
import itertools

import local_config

_address = "postgresql+psycopg2://{name}:{password}@{host}/{database}".format(
    name = local_config.DB_USER,
    password = local_config.DB_PASS,
    host = local_config.DB_HOST,
    database = local_config.DB_DB
)

_engine = sqlalchemy.create_engine( _address )
_metadata = sqlalchemy.MetaData( _engine )
_comments = sqlalchemy.Table( "comments", _metadata, autoload = True )
_downloads = sqlalchemy.Table( "downloads", _metadata, autoload = True )

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

_delete_comment = sqlalchemy.\
    delete( _comments ).\
    where( _comments.c.id == sqlalchemy.bindparam( "deleted_id" ) )

_approve_comment = sqlalchemy.\
    update( _comments ).\
    where( _comments.c.id == sqlalchemy.bindparam( "approved_id" ) ).\
    values( approved = True, spam = False )

_connection = _engine.connect()

#   Public functions

def get_comments( post ):
    """
    Returns list of comments for a specific post.
    
    Comments only contain public information and are sorted by time.
    """
    
    res = []
    for time, author, content, url in _connection.execute( _select_comments, post = post ):
        res.append( {
                "time":  time.isoformat(),
                "author": author,
                "content": content,
                "url": url
            } )
    return res

def new_comment( post, data, spam = False ):
    """
    Create a new comment, using mostly the data in "data".
    """
    
    defaulted_data = {
        "url": None,
        "referrer": ""
    }
    defaulted_data.update( data )
    _connection.execute( _comments.insert().values( post = post, spam = spam, approved = False, **defaulted_data ) )

#   Admin functions

def get_unapproved_comments():
    """
    Returns list of all unapproved comments.
    
    Unlike get_comments() this returns *all* columns since it's for administrative use.
    """
    
    result = []
    response = _connection.execute( _comments.select( _comments.c.approved == False ) )
    for row in response:
        comment = { column : value for column, value in itertools.izip( response.keys(), row ) }
        comment[ "time" ] = comment[ "time" ].isoformat()
        result.append( comment )
    response.close()
    return result

def trash_comment( id ):
    return _connection.execute( _delete_comment, deleted_id = id ).rowcount > 0

def approve_comment( id ):
    return _connection.execute( _approve_comment, approved_id = id ).rowcount > 0
