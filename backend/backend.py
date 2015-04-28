import flask
import logging

import just_mail
import just_akismet
import just_database
import local_config
import json

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

legacy_downloads = {
    "blender-249-ase-importer": 108,
    "blender-249-roff-im-exporter": 89,
    "blender-258a-md3-exporter-15": 395,
    "blender-262-md3-exporter-151": 284,
    "blender-262-roff-im-exporter": 39,
    "blender-264a-jedi-academy-suite": 173,
    "fluttershy-jedi-academy-playermodel": 95,
    "hard-reset-no-intro-mod": 437,
    "jkja-map-pack-1": 71,
    "lovedeathzombies": 67,
    "maze-game": 58,
    "mini-blue-box-boy-ld22": 107,
    "pysixense-33": 238,
    "razer-hydra-directinput-wrapper-05": 7068,
    "sith-lightsaber": 122,
    "wildfire-simulation": 46,
    "year-of-the-rooster": 65
}

#just_mail.send( "another test", "test 123" )
"""
test_data = akismet_defaults_comment.copy()
test_data.update( {
    "author": "a legit user",
    "user_ip": "localhost",
    "user_agent": "python script",
    "comment_content": "I like the new website design. And a custom AngularJS comment system with a Flask-based REST-backend? Nifty!\n\nWilli"
} )
print( just_akismet.check( test_data ) )
"""

app = flask.Flask( __name__ )

app.secret_key = local_config.SESSION_KEY

@app.route( "/rest/blog/<year>/<slug>/comments", methods = [ 'GET' ] )
def get_comments( year, slug ):
    post = "/".join( ( year, slug ) )
    response = flask.make_response( json.dumps( just_database.get_comments( post ) ), 200 )
    response.headers[ "Content-Type" ] = "application/json"
    return response

if __name__ == "__main__":
    app.run()
