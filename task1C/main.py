from flask import Flask, request, send_file, jsonify
from flask_uploads import UploadSet, configure_uploads
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ritesh'  
app.config['UPLOADED_FILES_DEST'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

files = UploadSet('files', ('txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'))
configure_uploads(app, files)

@app.route('/', methods=['GET'])
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            routes.append({'endpoint': rule.endpoint, 'methods': ','.join(rule.methods), 'path': str(rule)})
    return jsonify({'routes': routes})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file and files.file_allowed(file, file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOADED_FILES_DEST'], filename))
        return f'File uploaded successfully: {filename}', 200
    else:
        return 'Invalid file type', 400

@app.route('/download/<path:filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(os.path.join(app.config['UPLOADED_FILES_DEST'], filename), as_attachment=True)
    except FileNotFoundError:
        return 'File not found', 404

if __name__ == '__main__':
    app.run(debug=True)
