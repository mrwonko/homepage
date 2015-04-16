"""
@Author: Willi Schinmeyer

Adds some more python functions to the Jinja context.
"""

from pelican import signals

def adjust_context( pelican ):
    pelican.settings[ 'len' ] = len
    pelican.settings[ 'round' ] = round

def register():
    signals.initialized.connect( adjust_context )
