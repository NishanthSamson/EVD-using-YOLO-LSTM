from flask import Flask, render_template, request, redirect, url_for, session
from mp3 import convert_to_mp3
from EVD import lstm_prediction
from yolo8 import predict


from threading import Thread


app = Flask(__name__)
app.secret_key = 'nevergonnagiveyouup'


def lstm(file_path, result):
    convert_to_mp3(file_path)
    result.append(lstm_prediction())


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    file_path = "uploads/test.avi"
    uploaded_file = request.files['file']
    if uploaded_file:
        result = []
        uploaded_file.save(file_path)
        # predict(file_path)

        predict_thread = Thread(target=predict, args=(file_path,))
        lstm_thread = Thread(target=lstm, args=(file_path, result))

        predict_thread.start()
        lstm_thread.start()

        predict_thread.join()
        lstm_thread.join()

        # convert_to_mp3(file_path)
        # a = lstm_prediction()

        session['flag'] = 1
        session['vehicle'] = result[0]
        return redirect(url_for('results'))
    else:
        return "INVALID FILE UPLOAD"


@app.route('/results')
def results():

    flag = session.get('flag', 0)
    vehicle = session.get('vehicle')

    if (flag == 1):
        return render_template('results.html', vehicle=vehicle)
    else:
        return redirect(url_for('index'))


@app.route('/about')
def about():
    return render_template('about.html')


if (__name__ == '__main__'):
    app.run(debug=True)
