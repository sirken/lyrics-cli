#!/usr/bin/python3

from lyrics_extractor import Song_Lyrics
import sys
import tkinter as tk

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

#print(song_title)
#print(song_lyrics)

# Open the main window & start the Tcl interpreter
root = tk.Tk()

# Make a Frame to hold the Text widget and its Scrollbar
frame = tk.Frame(root)
frame.pack()

# Add the Scrollbar first so that it doesn't
# disappear when the window width is small
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add the Text widget
viewer = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set)
viewer.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Connect the Scrollbar to the Text widget
scrollbar.config(command=viewer.yview)

# Get the file name from the command line
#fname = sys.argv[1]

# Read the text file and add its contents to the Text widget
viewer.insert(tk.END, song_title + "\r\n\r\n" + song_lyrics)

root.mainloop()
