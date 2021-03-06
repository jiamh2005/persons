#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a _very simple_ example of a web service that recognizes faces in uploaded images.
# Upload an image file and it will check if the image contains a picture of Barack Obama.
# The result is returned as json. For example:
#
# $ curl -XPOST -F "file=@obama2.jpg" http://127.0.0.1:5001
#
# Returns:
#
# {
#  "face_found_in_image": true,
#  "is_picture_of_obama": true
# }
#

import os
from flask import Flask, jsonify, request, redirect, send_from_directory
from werkzeug import secure_filename
from landmark import landmark

from modules.filenamegen import nsfile, file_extension
from modules.storage.storage import *

# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt'}
UPLOAD_FOLDER = 'static/imgdata'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object(__name__)
app.config.from_envvar('PERSONS_SETTINGS', silent=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return save_faces_and_image(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>请上传照片，我们将在后台为您处理！！</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

def save_faces_and_image(file_stream):

    filenames = nsfile(1)
    fname = filenames[0]+file_extension(file_stream.filename)
    file_stream.save(os.path.join(app.config['UPLOAD_FOLDER'], fname))
    landmark(os.path.join(app.config['UPLOAD_FOLDER'], fname))

    # Return the result as json
    result = {
        "face_found_in_image": "no",
        "is_picture_of_obama": "no"
    }
    return jsonify(result)

@app.route('/api/v1/persons', methods=['GET'])
def get_persons():
    results = GetAllPersonFaces()
    persons = []
    for p in results :
        p['_id'] = ' '
        print p
        print '-----------------------------'
        persons.append(p)
    return jsonify(persons)

## 带参数的写法
## tasks/(?P<resource_id>\d+)/voters


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
