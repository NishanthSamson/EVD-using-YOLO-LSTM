from flask import Flask, render_template, request, redirect, url_for
from mp3 import convert_to_mp3
from EVD import lstm_prediction
from yolo8 import predict


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file_path = "uploads/test.avi"
    uploaded_file = request.files['file']
    if uploaded_file:
        uploaded_file.save(file_path)
        predict(file_path)
        convert_to_mp3(file_path)
        a = lstm_prediction()
    return redirect(url_for('view', vehicle = a))

@app.route('/view/<vehicle>')
def view(vehicle):
    return render_template('view.html', vehicle = vehicle)


if(__name__ == '__main__'):
    app.run(debug = True)