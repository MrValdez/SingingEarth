from flask import (Flask, 
                   render_template,
                   Response,
                   stream_with_context)
import time
import wikipedia
import random

app = Flask(__name__)

music_list = []
music_list = ["songs/Work.webm"]
default_song = "songs/dolphins.webm"
default_query = "dolphins"

@app.route('/music')
def music():
    audio_extension = "webm"

    def stream():
        global music_list
        while True:
            if len(music_list):
                song = music_list.pop(0)
            else:
                song = default_song

            with open(song, "rb") as file:
                data = file.read(1024)
                while data:
                    yield data
                    data = file.read(1024)
            if song == default_song:
                time.sleep(100)
                

    return Response(stream_with_context(stream()),
                    mimetype='audio/' + audio_extension)

@app.route('/')
def index():
    return render_template('camera.html')

@app.route('/info')
def info():
    query = "Philippines"
    
    query = None
    query = query if query is not None else default_query

    print("Searching Wikipedia")
    results = wikipedia.search(query, results=5)
    if results is None:
        results = [wikipedia.search(default_query, results=3, suggestion=True)]
    print("Found searches: {}".format(results))

    wiki_page = random.choice(results)
    wiki = wikipedia.page(wiki_page, auto_suggest=True, redirect=True)

    print("Loading wikipedia page: " + wiki_page)
    html = u"""<center><b>{}</b></center>
               <hr>
               <center>{}</center>
               <br>
               {}"""
    images = wiki.images
    random.shuffle(images)
    images_html = ["<img src={} width='200px'/>".format(image)
                   for image in images[:10]]
    images_html = "".join(images_html)
    #html = html.format(wiki.title, wiki.html())
    html = html.format(wiki.title, images_html, wiki.summary)
    return html

#@app.route('/get_isis')
#def 

if __name__ == '__main__':
    app.run(port=80, debug=True)