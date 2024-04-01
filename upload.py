#to send online, open cmd prompt type in ngrok http 5000 then enter
#alt paste this in to use https://promptly-promoted-husky.ngrok-free.app link
#     ngrok tunnel --label edge=edghts_2eSOqHswFI8cpQxpxVNEEstbKAi http://192.168.1.36:5000
from flask import Flask, request, render_template, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

PASSWORD = "Chand Raat by Uzma 2024"
USERS_FILE = "users.txt" 

# Specify the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def signin():
    return render_template('signin.html')

@app.route('/WackaFlockaFlame')
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
    return redirect('/gallery')

@app.route('/gallery')
def gallery():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Your authentication logic here
    print("Username:", username)
    print("Password:", password)
    if password == PASSWORD:
        # Store username in the text file
        with open(USERS_FILE, 'a') as f:
            f.write(username + '\n')
        # Redirect to index page if password is correct
        return render_template('index.html')
    else:
        # Redirect back to login page with error message
        return render_template('signin.html', error="Invalid password.")


@app.route('/uploads/<filename>')
def display_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi', 'mkv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

