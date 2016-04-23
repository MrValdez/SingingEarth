import re
import urllib
from collections import namedtuple

import billboard

song_info = namedtuple('song_info',
                       'name artist spotify url')

billboard_countries = [("us", "hot-100"),
                       ("japan", "japan-hot-100"),
                       ("china", "china-v-chart"),
                       ("uk", "united-kingdom-songs"),
                       ("uk", "united-kingdom-albums"),
                       ("canada", "hot-canada-digital-songs"),
                       ("canada", "canadaian-albums"),
                       ("germany", "germany-songs"),
                       ("germany", "germany-albums"),
                       ("france", "france-songs"),
                       ]


def _grab_billboard(country):
    billboard_url = [url for key, url in billboard_countries
                     if key == country.lower()]

    if not len(billboard_url):
        return None

    songs = [billboard.ChartData(url) for url in billboard_url]
    songs = [song[0] for song in songs]
    songs = [song_info(name=song.title,
                       artist=song.artist,
                       spotify=song.spotifyLink,
                       url=_find_url(song.title))
             for song in songs]

    return songs


def _grab_data(country):
    '''
        responsible for choosing the source to get song information
        returns a list of songs to play.
    '''
    songs = _grab_billboard(country)
    if songs is not None:
        return songs
    return None


def _find_url(title):
    '''
    return the youtube url of song
    '''
    # http://www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
    query_string = urllib.parse.urlencode({"search_query": title})
    url = "http://www.youtube.com/results?" + query_string
    html_content = urllib.request.urlopen(url)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})',
                                html_content.read().decode())
    url = ["http://www.youtube.com/watch?v=" + id for id in search_results]
    return url[0]


def grab(country):
    '''
        returns one song and the player
    '''
    songs = _grab_data(country)
    return songs[0]
