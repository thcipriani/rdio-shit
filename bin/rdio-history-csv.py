#!/usr/bin/env python2
"""
  rdio-history-csv.py
  ~~~~~~~~~~~~~~~~~~~

  Simple script for parsing the output of
  https://www.rdio.com/api/1/getHistoryForUser

  The way I made this happen was:
  #. login to rdio.com in chrome,
  #. visit https://www.rdio.com/people/tylercipriani/history/ with devtools
     open
  #. right click the 'getHistoryForUser' item in the network tab,
  #. "copy as cURL"
  #. Remove the "Accept-Encoding" header (don't want gzip)
  #. Change the "count=10" parameter to "count=9999999"
  #. redirect the output to "rdio-history.json"
  #. Run this script, redirect output to "rdio-history.csv"
  #. ???
  #. Profit.
"""

import os
import json

def process(string):
    return string.encode('ascii', 'ignore').replace(',', '').replace('"','').replace("'",'')

print "Date Played,Artist,Title,Album"
history_fmt = '{time},{artist},{title},{album}'
NA = 'N/A'

history_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '..', 'raw', 'rdio-history-raw.json'))

with open(history_path, 'r') as f:
    json_data = json.load(f)

sources = json_data['result']['sources']

for source in sources:
    tracks = source['tracks']['items']
    for track in tracks:
        info = track['track']
        print history_fmt.format(**{
            'time': process(track.get('time', NA)),
            'artist': process(info.get('artist', NA)),
            'title': process(info.get('name', NA)),
            'album': process(info.get('album', NA)),
        })
