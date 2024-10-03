"""
@Author: Willi Schinmeyer

Enable {filename} in article metadata listed in LINK_METADATA setting

Since there's no markup in metadata (besides summary), you can only mark the full string as a local link by prefixing it with {filename}.
"""

from pelican import signals
from pelican.utils import memoized
from pelican.contents import Content
import sys
if sys.version_info < (3, 0):
    from itertools import ifilter as filter
from six.moves.urllib.parse import urlparse, urlunparse
import logging
import os

logger = logging.getLogger( __name__ )

PREFIX = "{filename}"

# memoization of results cuts down on calculations at the cost of saving previous metadata values
@memoized
def update_content( article, content, siteurl ):
    self = article
    
    stripped_content = content.strip()
    if not stripped_content.startswith( PREFIX ):
        return content
    
    # remove {filename}
    url = stripped_content[ len( PREFIX ): ]
    
    parse_result = urlparse( url )
    path = parse_result.path
    
    if path.startswith( '/' ):
        path = path[ 1: ]
    else:
        # relative link
        path = self.get_relative_source_path( os.path.join( self.relative_dir, path ) )
    
    # unescape spaces if necessary
    if path not in self._context[ 'static_content' ]:
        path = path.replace( '%20', ' ' )

        if path not in self._context[ 'static_content' ]:
            logger.warning(
                f"Unable to find `{url}`, skipping url replacement.",
                extra = { 'limit_msg': ( "Other resources were not found and their urls not replaced" ) }
            )
            return content
    
    linked_content = self._context[ 'static_content' ][ path ]
    parts = list( parse_result )
    parts[ 2 ] = '/'.join( [ siteurl, linked_content.url ] )
    return urlunparse( parts )

def fix_metadata( self ):
    if 'LINK_METADATA' not in self.settings:
        logger.warning( "No LINK_METADATA set, metadata_links plugin won't do anything!" )
        return
    
    valid_keys = set( self.settings[ 'LINK_METADATA' ] )
    
    logger.debug( "Enabling links in metadata of {} articles".format( len( self.articles ) ) )
    
    #   save / remove current values
    for article in self.articles:
        article._mrw_metadata_attributes = {}
        for key in filter( lambda key: key in valid_keys, article.metadata.keys() ):
            # rename save_as and url like Content.__init__() does
            if key in [ 'save_as', 'url' ]:
                key = 'override_' + key
            # save initial value
            article._mrw_metadata_attributes[ key ] = getattr( article, key )
            # remove attribute, so class property is used for lookup
            delattr( article, key )

    #   Add Property to class
    
    
    def make_property( key ):
        def setter( self, value ):
            self._mrw_metadata_attributes[ key ] = value
            
        def getter( self ):
            if key not in self._mrw_metadata_attributes:
                return None
            return update_content( self, self._mrw_metadata_attributes[ key ], self.get_siteurl() )
        
        def deleter( self ):
            del self._mrw_metadata_attributes[ key ]
        
        return property( getter, setter, deleter )
    
    for key in valid_keys:
        logger.debug( "* enabled linking in '%s' metadata", key )
        # create property
        setattr( Content, key, make_property( key ) )

def register():
    signals.article_generator_pretaxonomy.connect( fix_metadata )
