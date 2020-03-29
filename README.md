# Lyrics Search for the CLI

A basic CLI lyrics search in Python 3, using the [lyrics-extractor](https://github.com/Techcatchers/PyLyrics-Extractor) library.

Because I spend a lot of time in the terminal, I wanted the most straight-forward way to search for lyrics from the CLI without having to know the exact song name, or even the exact spelling. The only thing returned are lyrics for the best match.

## Key features:

* CLI-only version
* TK GUI version as well
* Library supports flexible input (mix and match artist and song terms)
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

Search using artist and any song title words:
    ```console
    python3 lyrics.py artist song title
    ```

Or execute directly:
    ```console
    ./lyrics.py artist song title
    ```

Search using any song title words:
    ```console
    ./lyrics.py song title words
    ```

Or run without input get a prompt:
    ```console
    ./lyrics.py
    Lyrics search:
    ```
