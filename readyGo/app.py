from flask import Flask, render_template, Response, request, jsonify, redirect, url_for
# from camera import VideoCamera
import time
from flask_cors import CORS
import file_system as fs
from reg_finish import finish_registraion
import json
import face_recognition_knn as fkn


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('ticket.html')


@app.route('/done', methods=['POST', 'GET'])
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


@app.route('/admin_data', methods=['POST', 'GET'])
def get_users():
    if request.method == 'POST':
        print("GET in admin")
        print(jsonify(fs.data))
        finish_registraion()
        # return render_template('admin.html', data=data)
        return json.dumps(fs.data)



@app.route('/admin', methods=['POST', 'GET'])
def get_users_data():
    if request.method == 'GET':
        print("GET in admin")
        print(jsonify(fs.data))
        finish_registraion()
        # return render_template('admin.html', data=data)
        return json.dumps(fs.data)
    if request.method == 'POST':
        test = request.data
        try:
            test = test.decode()
            status = int(request.data)
            print(status)
            if not status:
                print('huhjhrjlhecljck;j;jcfpjejljrvliejvpivjeilvjievjievjijvipe')
                fkn.train('./train_dir', model_save_path='faces_prediction_model.pckl', verbose=True)
                finish_registraion()
            return "done"
        except AttributeError:
            print("qwertyuicvbnmfghjkk")
            print(request.data)
            return "done"





if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
