#!/usr/bin/python3

from lyrics_extractor import SongLyrics
from subprocess import Popen, PIPE
import sys

# API and Search engine
extract_lyrics = SongLyrics("API-KEY", "ENGINE-ID")

query = ""

# Check for cli arguments, [0] is always filename
if len(sys.argv) > 1:
    args = sys.argv
    for a in args[1:]:
        query = query + " " + a
# Otherwise, prompt for input
else:
    query = input("Lyrics search: ")

try:
    song = extract_lyrics.get_lyrics(query)
    final_lyrics = song['title'] + '\n' + song['lyrics']
    ps = Popen(("echo", final_lyrics), stdout=PIPE)
    output = Popen(('less'), stdin=ps.stdout)
    output.communicate()
except Exception as e:
    print(e)
