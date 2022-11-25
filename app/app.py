import os
import script
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

app=Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Get current path
path = "/Users/pranavaggarwal/Downloads/json-transformation-main/data/app"
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['json','csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def check_ext(filename,ext):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in [ext]


@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])

def my_form_post():
    text = request.form['text']
    return text



@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')
        locationa=""
        locationb=""
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                loca=os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(loca)
                if check_ext(file.filename,"json"):
                    locationa=loca
                else:
                    locationb=loca
        #script.main(locationa,locationb,my_form_post())
        
        flash('Files successfully processed')
        return redirect('/')


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)