from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
# from camera import VideoCamera
import time
from flask_cors import CORS
import file_system as fs
from reg_finish import finish_registraion
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('ticket.html')


@app.route('/done')
def done():
    return render_template('ticket_done.html')


@app.route('/adm')
def admin():
    return render_template('admin.html')


@app.route('/registration', methods=['POST', 'GET'])
def add_blog_ajax():
    if request.method == 'POST':
        image = request.json['image']
        name = request.json['name']
        fs.write_photo(name, image)
        print(fs.data)
        print("redirect")
        return redirect(url_for('done'))
    elif request.method == 'GET':
        return render_template('ticket.html')


@app.route('/admin', methods=['POST', 'GET'])
def get_users_data():
    if request.method == 'GET':
        print(jsonify(fs.data))
        # return render_template('admin.html', data=data)
        return json.dumps(fs.data)
    if request.method == 'POST':
        test = request.data
        try:
            test = test.decode()
            print("dddddddd")
            status = int(request.data)
            if status:
                finish_registraion()
        except AttributeError:
            print(request.data)
            return "done"


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
    app.run(host='127.0.0.1', debug=True)
