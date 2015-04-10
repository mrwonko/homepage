"""
@Author: Willi Schinmeyer

Support for different Article Types, via metadata "type": a separation a level above categories, for when different kinds of articles should go on the same page.

I actually completely ditch the ArticleGenerator's usual variables (articles etc.) except for authors and manually do the page creation
"""

from pelican import signals
from collections import defaultdict
from itertools import groupby as uniq, ifilter, imap, chain
from functools import partial
from operator import attrgetter
import logging

logger = logging.getLogger( __name__ )

def identity( x ):
    """
    A function that returns its parameter unchanged
    """
    return x

def constant( x ):
    """
    Returns a function that always returns x
    """
    return lambda: x

def fst( (x, _) ):
    return x

def snd( (_, x) ):
    return x

def group_by( keyfunc, iterable ):
    return uniq( sorted( iterable, key = keyfunc ), keyfunc )

class ArticleType:
    def __init__( self, articles, reverse_dates ):
        self.articles = sorted( articles, key = attrgetter('date'), reverse = True )
        
        self.dates = sorted( articles, key = attrgetter( "date" ), reverse = reverse_dates )
        
        self.articles_by_category = {
            category: list( cat_articles ) # groupby returns an iterator, turn that into a list
            for category, cat_articles in group_by(
                attrgetter( "category" ),
                articles
            )
        }
        self.articles_by_tag = defaultdict( list )
        for article in articles:
            if hasattr( article, "tags" ):
                for tag in article.tags:
                    self.articles_by_tag[ tag ].append( article )

def taxonomy( article_generator ):
    # called after articles have been read, before calculating tags & categories
    
    self = article_generator
    
    self.types = {
        type: ArticleType( list( articles ), self.context[ "NEWEST_FIRST_ARCHIVES" ] )
        for type, articles in group_by(
            attrgetter( "type" ),
            # only take articles that have the "type" metadata
            ifilter(
                lambda article: hasattr( article, "type" ),
                self.articles
            )
        )
    }
    
    # { AuthorName: { TypeName: [ Article } }
    self.articles_by_type_by_author = defaultdict( partial( defaultdict, list ) )
    
    for type, info in self.types.items():
        for article in info.articles:
            # add to authors' (type-partitioned) article lists
            for author in getattr( article, "authors", [] ):
                self.articles_by_type_by_author[ author ][ type ].append( article )
    
    for author, types in self.articles_by_type_by_author.items():
        for type, articles in types.items():
            articles.sort( key = attrgetter('date'), reverse = True )
    
    self._update_context( ( "types", "articles_by_type_by_author" ) )
    
    # we essentially want to overwrite the normal taxonomy phase, so let's empty the list used there
    self.articles = []
    # TODO: support translations
    self.translations = []

def write_articles_and_feeds( article_generator, writer ):
    # Called after default Articles and Feeds have been written.
    
    self = article_generator
    
    write_file = partial( writer.write_file, relative_urls = self.settings[ "RELATIVE_URLS" ] )
    
    def get_type_settings( type ):
        settings = {
            "index_save_as": type,
            "index_template": "index",
            "article_template": "article",
            "paginate": True
        }
        if "TYPES" in self.settings and type in self.settings[ "TYPES" ]:
            settings.update( self.settings[ "TYPES" ][ type ] )
        return settings
    
    def write_articles():
        pass
    
    def write_feeds():
        pass
    
    write_articles()
    write_feeds()

# entry point: define signals to listen to
def register():
    signals.article_generator_pretaxonomy.connect( taxonomy )
    signals.article_writer_finalized.connect( write_articles_and_feeds )
