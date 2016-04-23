# http://willdrevo.com/downloading-youtube-and-soundcloud-audio-with-python-and-pandas/
import os
import youtube_dl

def get_file(song):
    '''
    returns the file for song.
    if its not available, download it first.
    '''
    filedir = "songs/"
    filename = "{}/{}.{}".format(filedir, song.name, "mp3")

    if os.path.isfile(filename):
       return filename
 
    if not os.path.isdir(filedir):
        os.mkdir(filedir)

    tempfile = 'tmp_song.%(ext)s'
    options = {'nocheckcertificate': True,
               #'quiet': True,
               #'nowarnings': True,
               #'simulate': True,
               'extractaudio': True,
               # 'format': 'bestaudio/best',
               'format': 'bestaudio',
               'audioformat': 'mp3',
               'prefer_ffmpeg': True,
               'outtmpl': tempfile,
               }

    with youtube_dl.YoutubeDL(options) as ydl:
        result = ydl.extract_info(song.url, download=False)
        filename = "{}/{}.{}".format(filedir, song.name, result['ext'])

        if not os.path.isfile(filename):
            # print("Downloading song at {}".format(filename))
            result = ydl.extract_info(song.url, download=True)
            os.rename(tempfile % (result), filename)

    return filename