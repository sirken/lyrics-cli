#!/usr/bin/python3

from lyrics_extractor import Song_Lyrics
import sys

# API and Search engine
extract_lyrics = Song_Lyrics("API-KEY", "ENGINE-ID")

query = ""

# Check for cli arguments, [0] is always filename
if len(sys.argv) > 1:
	args = sys.argv
	for a in args[1:]:
		query = query + " " + a
# Otherwise, prompt for input
else:
    query = input("Lyrics search: ")

song_title, song_lyrics = extract_lyrics.get_lyrics(query)

print(song_title)
print(song_lyrics)
