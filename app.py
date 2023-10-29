from flask import Flask, render_template, request, redirect, url_for, session
from mp3 import convert_to_mp3
from EVD import lstm_prediction
from yolo8 import predict


app = Flask(__name__)
app.secret_key = 'nevergonnagiveyouup'

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
        session['flag'] = 1
        session['vehicle'] = a
        return redirect(url_for('results'))
    else:
        return "INVALID FILE UPLOAD"

@app.route('/results')
def results():

    flag = session.get('flag', 0)
    vehicle = session.get('vehicle')
    
    if(flag==1):
        return render_template('results.html', vehicle = vehicle)
    else:
        return redirect(url_for('index'))

if(__name__ == '__main__'):
    app.run(debug = True)