from flask import Flask, render_template, Response, request, jsonify
# from camera import VideoCamera
import time
from flask_cors import CORS
from file_system import write_photo


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['POST', 'GET'])
def add_blog_ajax():
    if request.method == 'POST':
        image = request.json['image']
        name = request.json['name']
        write_photo(name, image)
        return "Done"


@app.route('/admin', methods=['POST', 'GET'])
def get_users_data():
    if request.method == 'GET':
        data = [
            {
                'name': 'Igor',
                'available': '1',
            },
            {
                'name': 'Sveta',
                'available': '0',
            }
        ]
        print(jsonify(data))
        # return render_template('admin.html', data=data)
        return (jsonify(data))
    

def gen(camera):
    while True:
        time.sleep(0.5)
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
