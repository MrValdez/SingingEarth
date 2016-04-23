import os
import song
import youtube_dl

country = 'us'
print("Looking for songs in the country of {}".format(country))
song = song.grab(country)

# http://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas/
tempfile = 'tmp_song.%(ext)s'

options = {'nocheckcertificate': True,
           'quiet': True,
           'nowarnings': True,
           # 'simulate': True,
           'extractaudio': True,
           # 'format': 'bestaudio/best',
           'format': 'bestaudio',
           'audioformat': 'mp3',
           'outtmpl': tempfile,
           }

filedir = "songs/"
if not os.path.isdir(filedir):
    os.mkdir(filedir)

print("Downloading song")
with youtube_dl.YoutubeDL(options) as ydl:
    result = ydl.extract_info(song.url, download=False)
    filename = "{}.{}".format(song.name, result['ext'])

    if not os.path.isfile(filedir + filename):
        result = ydl.extract_info(song.url, download=True)
        os.rename(tempfile % (result), filedir + filename)

print("Playing \"{}\" by {}".format(song.name, song.artist))
