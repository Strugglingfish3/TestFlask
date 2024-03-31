#to send online, open cmd prompt type in ngrok http 5000 then enter
#alt paste this in to use https://promptly-promoted-husky.ngrok-free.app link
#ngrok tunnel --label edge=edghts_2eSOqHswFI8cpQxpxVNEEstbKAi http://192.168.1.36:5000
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Specify the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('files[]')
    for file in files:
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return 'Files uploaded successfully'

@app.route('/gallery')
def gallery():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

@app.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

