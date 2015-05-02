import itertools
from txpostgres import txpostgres, reconnection
from twisted.internet import reactor, defer
from twisted.python import log

import just_akismet

import local_config

_connection = None
_comment_columns = [ "id", "post", "spam", "user_agent", "referrer", "author", "time", "email", "url", "content", "approved", "ip" ]
_comment_columns_string = ", ".join( _comment_columns ) 
def _comment_row_to_dict( row ):
    comment = { column : value for column, value in itertools.izip( _comment_columns, row ) }
    comment[ "time" ] = comment[ "time" ].isoformat()
    return comment

#   Public functions
@defer.inlineCallbacks
def connect():
    global _connection
    _connection = txpostgres.Connection( detector = reconnection.DeadConnectionDetector() )
    yield _connection.connect(
        host = local_config.DB_HOST,
        port = local_config.DB_PORT,
        user = local_config.DB_USER,
        password = local_config.DB_PASS,
        dbname = local_config.DB_DB
    )

@defer.inlineCallbacks
def get_comments( post ):
    """
    Returns list of comments for a specific post.
    
    Comments only contain public information and are sorted by time.
    """
    
    res = []
    rows = yield _connection.runQuery( 
        """SELECT time, author, content, url
        FROM comments
        WHERE post = %s and approved = true
        ORDER BY time ASC;""",
        [ post ]
    )
    for time, author, content, url in rows:
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
    defaulted_data[ "post" ] = post
    defaulted_data[ "spam" ] = spam
    defaulted_data[ "approved" ] = False
    keys = []
    values = []
    for key, value in defaulted_data.items():
        keys.append( key )
        values.append( value )
    key = yield _connection.runQuery(
        """INSERT INTO comments( {keys} )
        VALUES ( {values} )
        RETURNING id""".format(
            keys = ", ".join( keys ),
            values = ", ".join( [ "%s" ] * len( values ) )
        ),
        values
    )
    defer.returnValue( key )

@defer.inlineCallbacks
def get_download_count( name ):
    rows = yield _connection.runQuery(
        """SELECT COUNT( * )
        FROM downloads JOIN download_names ON downloads.download = download_names.id
        WHERE download_names.name = %s""",
        [ name ]
    )
    defer.returnValue( rows[ 0 ][ 0 ] )

@defer.inlineCallbacks
def new_download( name ):
    @defer.inlineCallbacks
    def get_or_create_name( cursor ):
        yield cursor.execute( 
            """SELECT id
            FROM download_names
            WHERE name = %s""",
            [ name ]
        )
        if cursor.rowcount > 0:
            row = yield cursor.fetchone()
            defer.returnValue( row[ 0 ] )
        else:
            yield cursor.execute(
                """INSERT INTO download_names( name )
                VALUES ( %s )
                RETURNING id""",
                [ name ]
            )
            row = yield cursor.fetchone()
            download_id = row[ 0 ]
            defer.returnValue( download_id )
    
    name_id = yield _connection.runInteraction( get_or_create_name )
    yield _connection.runOperation( 
        """INSERT INTO downloads( download )
        VALUES ( %s )""",
        [ name_id ]
    )
    defer.returnValue( None )

#   Admin functions

@defer.inlineCallbacks
def get_unapproved_comments():
    """
    Returns list of all unapproved comments.
    
    Unlike get_comments() this returns *all* columns since it's for administrative use.
    """
    
    rows = yield _connection.runQuery(
        """SELECT {}
        FROM comments
        WHERE approved = false
        ORDER BY time DESC""".format( _comment_columns_string )
    )
    result = []
    for row in rows:
        result.append( _comment_row_to_dict( row ) )
    defer.returnValue( result )


@defer.inlineCallbacks
def trash_comment( comment_id ):
    rows = yield _connection.runQuery(
        """DELETE FROM comments
        WHERE id = %s
        RETURNING {}""".format( _comment_columns_string ),
        [ comment_id ]
    )
    defer.returnValue( _comment_row_to_dict( rows[ 0 ] ) if len( rows ) > 0 else None )

def approve_comment( comment_id ):
    @defer.inlineCallbacks
    def get_and_approve( cursor ):
        yield cursor.execute(
            """SELECT {}
            FROM comments
            WHERE id = %s""".format( _comment_columns_string ),
            [ comment_id ]
        )
        if cursor.rowcount == 0:
            defer.returnValue( None )
        else:
            row = yield cursor.fetchone()
            comment = _comment_row_to_dict( row )
            if not comment[ "approved" ]:
                yield cursor.execute(
                    """UPDATE comments
                    SET approved = true, spam = false
                    WHERE id = %s""",
                    [ comment_id ]
                )
            defer.returnValue( comment )
    return _connection.runInteraction( get_and_approve )
