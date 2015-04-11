"""
@Author: Willi Schinmeyer

Support for different Article Types, via metadata "type": a separation a level above categories, for when different kinds of articles should go on the same page.

Adds {type} substitution to CATEGORY_URL, TAG_SAVE_AS etc.

I actually completely ditch the ArticleGenerator's usual variables (articles etc.) except for authors and manually do the page creation.

Known issues:
*   {category} and {tag} links don't work if the tag/category URL includes {type} since they create a new, type-agnostic URLWrapper object
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
    def __init__( self, name, articles, settings ):
        self.settings = {
            "index_save_as": "index",
            "index_template": "index",
            "tags_save_as": "tags", # set to none to disable tags page
            "tags_template": "tags",
            "categories_save_as": "categories", # set to None to disable categories page
            "categories_template": "categories",
            "article_template": "article",
            "feed_rss": None,
            "feed_atom": None
        }
        if "TYPES" in settings and name in settings[ "TYPES" ]:
            self.settings.update( settings[ "TYPES" ][ name ] )
        
        self.articles = sorted( articles, key = attrgetter('date'), reverse = True )
        
        self.dates = sorted( articles, key = attrgetter( "date" ), reverse = settings[ "NEWEST_FIRST_ARCHIVES" ] )
        
        self.articles_by_category = list( {
            category: list( cat_articles ) # groupby returns an iterator, turn that into a list
            for category, cat_articles in group_by(
                attrgetter( "category" ),
                articles
            )
        }.items() )
        self.articles_by_category.sort( reverse = settings[ "REVERSE_CATEGORY_ORDER" ] )
        
        self.articles_by_tag = defaultdict( list )
        for article in articles:
            if hasattr( article, "tags" ):
                for tag in article.tags:
                    self.articles_by_tag[ tag ].append( article )

def taxonomy( article_generator ):
    # called after articles have been read, before calculating tags & categories
    
    self = article_generator
    
    for article in self.articles:
        if hasattr( article, "type" ):
            # enable usage of {type} in CATEGORY_SAVE_AS/CATEGORY_URL
            # category comparison is done by name, so categories of different types would be merged in a dictionary
            # but we separate category dictionaries by type so that's no problem
            article.category.type = article.type
            if hasattr( article, "tags" ):
                for tag in article.tags:
                    tag.type = article.type
    
    self.types = {
        type: ArticleType( type, list( articles ), self.settings )
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
    
    for type, info in self.types.iteritems():
        for article in info.articles:
            # add to authors' (type-partitioned) article lists
            for author in getattr( article, "authors", [] ):
                self.articles_by_type_by_author[ author ][ type ].append( article )
    
    for author, types in self.articles_by_type_by_author.iteritems():
        for type, articles in types.iteritems():
            articles.sort( key = attrgetter('date'), reverse = True )
    
    # we overwrite the normal taxonomy phase, so we empty the list used there
    # the self.categories dict wouldn't distinguish categories of different types
    self.articles = []
    # TODO: support translations?
    self.translations = []

def write_articles_and_feeds( article_generator, writer ):
    # Called after default Articles and Feeds have been written.
    
    self = article_generator
    
    write_file = partial( writer.write_file, relative_urls = self.settings[ "RELATIVE_URLS" ] )
        
    for type, info in self.types.iteritems():
        logger.debug( "Processing {} articles".format( type ) )
        index_template = self.get_template( info.settings[ "index_template" ] )
        article_template = self.get_template( info.settings[ "article_template" ] )
        tags_template = self.get_template( info.settings[ "tags_template" ] ) if info.settings[ "tags_template" ] else None
        categories_template = self.get_template( info.settings[ "categories_template" ] ) if info.settings[ "categories_template" ] else None
        
        logger.debug( "* generating {} index page(s) ({})".format( type, info.settings[ "index_save_as" ] ) )
        # TODO
        
        logger.debug( "* generating {} article pages".format( type ) )
        # TODO
        
        logger.debug( "* generating {} category pages".format( type ) )
        logger.debug( "* generating {} tag pages".format( type ) )
        
        feed_rss = info.settings[ "feed_rss" ]
        if feed_rss:
            logger.debug( "* generating {} RSS feed {}".format( type, feed_rss ) )
            # TODO
        
        feed_atom = info.settings[ "feed_atom" ]
        if feed_atom:
            logger.debug( "*generating {} Atom feed {}".format( type, feed_atom ) )
            # TODO

# entry point: define signals to listen to
def register():
    signals.article_generator_pretaxonomy.connect( taxonomy )
    signals.article_writer_finalized.connect( write_articles_and_feeds )
