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

for album in albums:
    print format_str.format(**{
        'artist': album.get('artist', NA).encode('ascii', 'ignore'),
        'album': album.get('name', NA).encode('ascii', 'ignore'),
    })
