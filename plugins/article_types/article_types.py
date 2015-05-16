"""
@Author: Willi Schinmeyer

Support for different Article Types, via metadata "type": a separation a level above categories, for when different kinds of articles should go on the same page.

Adds {type} substitution to CATEGORY_URL, TAG_SAVE_AS etc.

Adds PAGINATE_AUTHOR_PAGES setting to disable pagination on individual author pages

I actually completely ditch the ArticleGenerator's usual variables (articles etc.) except for authors and manually do the page creation.

Known issues:
*   {category} and {tag} links don't work if the tag/category URL includes {type} since they create a new, type-agnostic URLWrapper object
*   Drafts are not supported.
"""

from pelican import signals
from collections import defaultdict
from itertools import groupby as uniq, ifilter, imap, chain
from functools import partial
from operator import attrgetter
import os
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
        title = settings[ 'index_title' ] if 'index_title' in settings else name
        self.settings = {
            'index_title': title,
            'index_save_as': os.path.join( name, "index.html" ),
            'index_template': "index",
            'index_paginate': True,
            
            # list of tags
            'tags_title': title + " - tags",
            'tags_save_as': os.path.join( name, "tags.html" ), # set to none to disable tags page
            'tags_template': "tags",
            'tags_paginate': False,
            # for individual tag pages
            'tag_template': "tag",
            'tag_paginate': False,
            
            # list of categories
            'categories_title': title + " - categories",
            'categories_save_as': os.path.join( name, "categories.html" ), # set to None to disable categories page
            'categories_template': "categories",
            'categories_paginate': False,
            # for individual category pages
            'category_template': "category",
            'category_paginate': False,
            
            'article_template': "article", # can be overwritten per-article via metadata as usual
            'feed_rss': None,
            'feed_atom': None,
        }
        if 'TYPE_SETTINGS' in settings and name in settings[ 'TYPE_SETTINGS' ]:
            self.settings.update( settings[ 'TYPE_SETTINGS' ][ name ] )
        
        self.articles = sorted( articles, key = attrgetter( 'date' ), reverse = True )
        
        self.dates = sorted( articles, key = attrgetter( 'date' ), reverse = settings[ 'NEWEST_FIRST_ARCHIVES' ] )
        
        self.articles_by_category = {
            category: sorted( cat_articles, key = attrgetter( 'date' ), reverse = True ) # groupby returns an iterator, turn that into a list & sort
            for category, cat_articles in group_by(
                attrgetter( "category" ),
                articles
            )
        }
        
        self.articles_by_tag = defaultdict( list )
        for article in articles:
            if hasattr( article, 'tags' ):
                for tag in article.tags:
                    self.articles_by_tag[ tag ].append( article )
        for tag, articles in self.articles_by_tag.items():
            articles.sort( key = attrgetter( 'date' ), reverse = True )

def taxonomy( article_generator ):
    # called after articles have been read, before calculating tags & categories
    
    self = article_generator
    
    for article in self.articles:
        if hasattr( article, 'type' ):
            # enable usage of {type} in CATEGORY_SAVE_AS/CATEGORY_URL
            # category comparison is done by name, so categories of different types would be merged in a dictionary
            # but we separate category dictionaries by type so that's no problem
            article.category.type = article.type
            if hasattr( article, 'tags' ):
                for tag in article.tags:
                    tag.type = article.type
    
    self.types = {
        type: ArticleType( type, list( articles ), self.settings )
        for type, articles in group_by(
            attrgetter( 'type' ),
            # only take articles that have the 'type' metadata
            ifilter(
                lambda article: hasattr( article, 'type' ),
                self.articles
            )
        )
    }
    
    # { AuthorName: { TypeName: [ Article } }
    self.articles_by_type_by_author = defaultdict( partial( defaultdict, list ) )
    
    for type, info in self.types.items():
        for article in info.articles:
            # add to authors' (type-partitioned) article lists
            for author in getattr( article, 'authors', [] ):
                self.articles_by_type_by_author[ author ][ type ].append( article )
    
    for author, types in self.articles_by_type_by_author.items():
        for type, articles in types.items():
            articles.sort( key = attrgetter('date'), reverse = True )
    
    self.mrw_all_articles = self.articles
    
    # we overwrite the normal taxonomy phase, so we empty the list used there
    # the self.categories dict wouldn't distinguish categories of different types
    self.articles = []
    # TODO: support translations?
    self.translations = []
    
    self._update_context( [ 'articles_by_type_by_author' ] )
    self.context[ 'types' ] = self.types

def write_articles_and_feeds( article_generator, writer ):
    # Called after default Articles and Feeds have been written.
    
    self = article_generator
    
    write_file = partial( writer.write_file, relative_urls = self.settings[ 'RELATIVE_URLS' ] )
    
    new_keys = ( 'type', 'type_settings' )
    previous_values = { key: self.context[ key ] for key in new_keys if key in self.context }
    
    for type, info in self.types.items():
        logger.debug( "Processing {} articles".format( type ) )
        
        # adjust context for this article type
        # we mustn't make a copy because articles hold a reference to the context, where they look up "SITEURL", which is changed by write_file() when using relative paths
        # we'll change it back after the loop
        context = self.context
        context[ 'articles' ] = info.articles
        context[ 'dates' ] = info.dates
        context[ 'categories' ] = list( info.articles_by_category.items() )
        context[ 'categories' ].sort( reverse = self.settings[ 'REVERSE_CATEGORY_ORDER' ] )
        context[ 'authors' ] = list( self.articles_by_type_by_author.get( type, {} ).items() )
        context[ 'authors' ].sort()
        context[ 'tags' ] = list( info.articles_by_tag.items() )
        context[ 'type' ] = type
        context[ 'type_settings' ] = info.settings
        
        paginated = { 'articles': info.articles, 'dates': info.dates }

        #   Articles
        # logger.debug( "* generating {} article pages".format( type ) )
        article_template = self.get_template( info.settings[ 'article_template' ] )
        for article in info.articles:
            signals.article_generator_write_article.send( self, content = article )
            write_file(
                article.save_as,
                # respect template: metadata, it overrules type.article_template
                article.metadata[ 'template' ] if 'template' in article.metadata and article.metadata[ 'template' ] is not None else article_template,
                context,
                article = article,
                category = article.category,
                override_output = hasattr( article, 'override_save_as' ),
                blog = True
            )
        
        #   Article Index, Categories Index, Tags Index
        for what in ( 'index', 'categories', 'tags' ):
            # logger.debug( "* generating {} {} page(s)".format( type, what ) )
            save_as = info.settings[ '{}_save_as'.format( what ) ]
            if save_as:
                write_file(
                    save_as,
                    self.get_template( info.settings[ '{}_template'.format( what ) ] ),
                    context,
                    blog = True,
                    paginated = paginated if info.settings[ '{}_paginate'.format( what ) ] else {},
                    page_name = info.settings[ '{}_title'.format( what ) ]
                )
        
        #   Categories, Tags
        for name, dict in [
            ( "category", info.articles_by_category ),
            ( "tag", info.articles_by_tag )
        ]:
            template = self.get_template( info.settings[ '{}_template'.format( name ) ] )
            paginate = info.settings[ '{}_paginate'.format( name ) ]
            for item, articles in dict.items():
                dates = [ article for article in info.dates if article in articles ]
                write_file(
                    item.save_as,
                    template,
                    context,
                    articles = articles,
                    dates = dates,
                    paginated = { 'articles': articles, 'dates': dates } if paginate else {},
                    blog = True,
                    page_name = item.page_name,
                    all_articles = info.articles,
                    **{ name : item }
                )
        
        #   RSS, Atom Feeds
        for ( name, feed_type ) in ( ( 'feed_rss', 'rss' ), ( 'feed_atom', 'atom' ) ):
            feed = info.settings[ name ]
            if feed:
                # logger.debug( "* generating {} {} feed {}".format( type, feed_type, feed ) )
                writer.write_feed( info.articles, context, feed, feed_type = feed_type )
        
        print( "Processed {} {} article(s)".format( len( info.articles ), type ) )
    
    #   Reset context (we changed these for each type)
    self._update_context( [ "articles", "dates", "tags", "categories", "authors" ] )
    for key in new_keys:
        if key in previous_values:
            self.context[ key ] = previous_values[ key ]
        else:
            del self.context[ key ]
    
    #   Authors
    author_template = self.get_template( 'author' )
    for author, articles_by_type in self.articles_by_type_by_author.items():
        articles = list( chain.from_iterable( articles_by_type.itervalues() ) )
        articles.sort( key = attrgetter( 'date' ), reverse = True )
        dates = list( articles )
        if not self.settings[ 'NEWEST_FIRST_ARCHIVES' ]:
            dates.reverse()
        
        write_file(
            author.save_as,
            author_template,
            self.context,
            author = author,
            articles = articles,
            dates = dates,
            paginated = { 'articles': articles, 'dates': dates } if self.settings.get( 'PAGINATE_AUTHOR_PAGES', True ) else {},
            page_name = author.page_name,
            all_articles = self.mrw_all_articles,
            articles_by_type = sorted( articles_by_type.items() )
        )

# entry point: define signals to listen to
def register():
    signals.article_generator_pretaxonomy.connect( taxonomy )
    signals.article_writer_finalized.connect( write_articles_and_feeds )
