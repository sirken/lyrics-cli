# Lyrics Search for the CLI

A basic CLI lyrics search in Python 3, using the [lyrics-extractor](https://github.com/Techcatchers/PyLyrics-Extractor) library.

Because I spend a lot of time in the terminal, I wanted the most straight-forward way to search for lyrics from the CLI without knowing the exact song name or title, or by searching for some of the lyrics. This script returns the lyrics of the best match for your search terms.

## Key features:

* CLI-only version
* TK GUI version as well
* Library supports flexible input (artist name, title, lyrics)
* Library can handle misspellings

## Prerequisites

* Install required [required libraries](https://github.com/Techcatchers/PyLyrics-Extractor/blob/master/README.md#installation)
* Create Google API key
* Create Engine ID

See the [lyrics-extractor readme](https://github.com/Techcatchers/PyLyrics-Extractor/blob/master/README.md#installation) for these prerequisites.

## Installation

1. Modify the script with your API key and Engine ID:
    ```python
    extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
    ```

2. If you want to execute the script directly:
    ```console
    chmod +x lyrics.py
    ```

3. (Optional) If you want to use the GUI script, install the python3-tk library for your distro (Debian for example):
    ```console
    sudo apt install python3-tk
    ```

## Usage Examples

Search using any combination of artist, title, or lyrics:
```console
python3 lyrics.py artist title lyrics
```

Or execute directly:
```console
./lyrics.py artist artist title lyrics
```

Search using song lyrics:
```console
./lyrics.py some song lyrics
```

Or run without input get a prompt:
```console
./lyrics.py
Lyrics search:
```
