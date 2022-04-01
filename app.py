import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def load_file():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['photo1d']
        f.save("./static/" + secure_filename(f.filename))
        return render_template('result.html', image_file= f.filename)

# @app.route('/result2', methods=['GET', 'POST'])
# def upload_file2():
#     if request.method == 'POST':
#         f = request.files['photo50d']
#         f.save("./static/" + secure_filename(f.filename))
#
#         return render_template('result2.html', image_file= f.filename)

if __name__ == '__main__':
    app.run(debug=True)