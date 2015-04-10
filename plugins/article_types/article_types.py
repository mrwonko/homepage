"""
@Author: Willi Schinmeyer

Support for different Article Types, via metadata "type": a separation a level above categories, for when different kinds of articles should go on the same page.

I actually completely ditch the ArticleGenerator's usual variables (articles etc.) except for authors and manually do the page creation
"""

from pelican import signals
from collections import defaultdict
from functools import partial
import logging

logger = logging.getLogger(__name__)

class ArticleType:
    def __init__( self ):
        self.articles = []
        # create an empty list when a non-existent category/tag is requested
        self.articles_by_category = defaultdict( list )
        self.articles_by_tag = defaultdict( list )

def article_generator_created( article_generator ):
    print( "Article Generator created! Adjust methods here." )
    pass

def skip_original_taxonomy( article_generator ):
    # called after articles have been read, before calculating tags & categories
    
    self = article_generator
    
    # we essentially want to overwrite the normal taxonomy phase, so let's empty the used lists, saving them first
    articles = self.articles
    self.articles = []
    
    # { TypeName: ArticleType }
    self.types = defaultdict( ArticleType )
    
    for article in articles:
        # Authors are the same across types, so we can fill this here and the original code will take care of the rest
        for author in getattr( article, "authors", [] ):
            self.authors[ author ].append( article )
        
        if not hasattr( article, "type" ):
            logger.error( "Article {} lacks type metadata! Skipping.".format( article.source_path ) )
            continue
        
        self.types[ article.type ].articles.append( article )
    
    def partition_by_type( articles ):
        articles_by_type = defaultdict( list )
        for article in articles:
            if hasattr( article, "type" ):
                articles_by_type[ article.type ].append( article )
        return articles_by_type
    self.articles_by_type_by_author = { author: partition_by_type( articles ) for ( author, articles ) in self.authors.items() }

def custom_taxonomy( article_generator ):
    # called after normal tag/category calculation is done (which mostly does nothing due to skip_original_taxonomy())
    
    self = article_generator
    
    # TODO calculate categories, tags
    
    self._update_context( ( "types", "articles_by_type_by_author" ) )
    self.save_cache()
    self.readers.save_cache()

def articles_written( article_generator, writer ):
    # Called after default Articles and Feeds have been written.
    
    self = article_generator
    
    # TODO generate pages, tags, 
    
    print( "Articles written. Write custom feeds now." )

# entry point: define signals to listen to
def register():
    signals.article_generator_init.connect( article_generator_created )
    signals.article_generator_pretaxonomy.connect( skip_original_taxonomy )
    signals.article_generator_finalized.connect( custom_taxonomy )
    signals.article_writer_finalized.connect( articles_written )
