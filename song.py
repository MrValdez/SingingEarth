from collections import namedtuple

import billboard

song_info = named_tuple('song-info',
                        'name artist spotify')

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
                       spotify=song.spotify)
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


def grab(country):
    '''
        returns one song and the player
    '''
    songs = _grab_data(country)
    return song[0]
