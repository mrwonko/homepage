from flask import Flask
import logging

import just_mail
import just_akismet
import local_config

logging.basicConfig()

logger = logging.Logger( __name__ )
logger.addHandler( logging.StreamHandler() ) # output to stdout/stderr

akismet_defaults_comment = {
    "blog": "http://mrwonko.de/blog",
    "blog_lang": "en",
    "blog_charset": "UTF-8",
    "comment_type": "comment"
}

akismet_defaults_contact = {
    "blog": "http://mrwonko.de/contact", # TODO
    "blog_charset": "UTF-8",
    "blog_lang": "en, de",
    "comment_type": "contact-form"
}

#just_mail.send( "another test", "test 123" )

test_data = akismet_defaults_comment.copy()
test_data.update( {
    "author": "a legit user",
    "user_ip": "localhost",
    "user_agent": "python script",
    "comment_content": "I like the new website design. And a custom AngularJS comment system with a Flask-based REST-backend? Nifty!\n\nWilli"
} )
print( just_akismet.check( test_data ) )