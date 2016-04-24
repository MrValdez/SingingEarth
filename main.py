from flask import (Flask, 
                   render_template,
                   Response,
                   stream_with_context)
from camera import Camera

app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(stream_with_context(gen(Camera())),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/music')
def music():
    audio_extension = "webm"

    def play():
        with open("songs/Work.webm", "rb") as song:
            data = song.read(1024)
            while data:
                yield data
                data = song.read(1024)

    return Response(stream_with_context(play()),
                    mimetype='audio/' + audio_extension)

@app.route('/')
def index():
    return render_template('camera.html')

#@app.route('/get_isis')
#def 

if __name__ == '__main__':
    app.run(port=80, debug=True)