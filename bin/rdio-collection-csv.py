#!/usr/bin/env python2
"""
    rdio-collection-csv.py
    ~~~~~~~~~~~~~~~~~~~~~~

    #. Download list of favorites:
       http://iangilman.com/rdio-exodus/export-favorite-albums/
    #. Run script
    #. Redirect output to rdio-collection.csv
    #. ???
    #. Profit.
"""

import os
import json

NA = 'N/A'

print 'Artist,Album'
format_str = '{artist},{album}'
collection_file = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '..', 'raw', 'rdio-collection-raw.json'))

with open(collection_file, 'r') as f:
    albums = json.load(f)

def process(string):
    return string.encode('ascii', 'ignore').replace(',', '').replace('"','').replace("'",'')

for album in albums:
    print format_str.format(**{
        'artist': process(album.get('artist', NA)),
        'album': process(album.get('name', NA))
    })
