import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from analyse import get_succes_not_success_calls_count

UPLOAD_FOLDER = '.\\uploads'
ALLOWED_EXTENSIONS = set(['xls', 'XLS'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def get_data(filename):
    success_cals_count, not_success_cals_count = get_succes_not_success_calls_count(
        os.path.join(app.config['UPLOAD_FOLDER'], filename))
    data = {'total_calls': success_cals_count + not_success_cals_count,
            'success_calls': success_cals_count,
            'not_success_calls': not_success_cals_count}
    return data


@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    filename = None
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)):
                os.remove(os.path.join(
                    app.config['UPLOAD_FOLDER'], file.filename))
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            data = get_data(filename)
            return render_template('upload.html', data=data)
    if request.method == 'GET':
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)
