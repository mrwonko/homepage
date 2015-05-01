# Flask Setup
HOST = "127.0.0.1"
PORT = 5000

# Akismet Setup
AKISMET_KEY = ""
AKISMET_ENABLED = False
AKISMET_CHECK_CERTS = True

# Database Setup
DB_HOST = "localhost"
DB_DB = ""
DB_USER = "root"
DB_PASS = ""

# SMTP/Mail Setup
SMTP_SERVER = ""
SMTP_USER = ""
SMTP_PASS = ""

MAIL_ENABLED = False

MAIL_TO = [ "" ]
MAIL_FROM = ""

MAIL_BODY_NEW_COMMENT = """\
New blog comment by {comment["author"]}, it's {spammy}.
"""

# Private key for session encryption
SESSION_KEY = 'secret'

# Previous Downloads
LEGACY_DOWNLOADS = {
    "files/sith_saber_bonez_v3.zip": 122,
    "files/blender_roff_imexport.zip": 89,
    "files/WildFireSim.zip": 46,
    "files/blender_ase_import.zip": 108,
    "files/YearOfTheRooster.zip": 65,
    "files/LoveDeathZombies.zip": 67,
    "files/Hydra-DirectInput-Wrapper-0.5.zip": 7068,
    "files/mrw_blender_2.64a_jediacademy_plugins.zip": 173,
    "files/hardreset_nointro.zip": 437,
    "files/0hgame-maze.zip": 58,
    "files/mrw_mappack.7z": 71,
    "files/blender_io_mesh_md3_15.zip": 395,
    "files/LD22mrw_0241.7z": 107,
    "files/blender_2.6_roff_addons.zip": 39,
    "files/fluttershy.pk3": 95,
    "files/blender_io_mesh_md3_151.zip": 284,
    "files/PySixense-Py33.zip": 238,
}

# Comment Settings
TAG_WHITELIST = sorted( [
    u'a',
    u'abbr',
    u'acronym',
    u'b',
    u'blockquote',
    u'code',
    u'em',
    u'i',
    u'li',
    u'ol',
    u'strong',
    u'ul',
    u'code',
    u'pre'
] )
ATTRIBUTE_WHITELIST = {
    u'a': [ u'href', u'title' ],
    u'acronym': [ u'title' ],
    u'abbr': [ u'title' ]
}