#!/usr/bin/python3
# can only run directly if numpy  and flask are installed

"""
JPMC Virtual SEP - InsideSherpa - Module 2
Pedro Teixeira - O734271

REST API for the sancions module
"""

import os

from flask import Flask, request
from werkzeug.utils import secure_filename
from sanctions import screen_name

UPLOAD_FOLDER = './lists/'
ALLOWED_EXTENSIONS = {'txt', 'csv'}

app = Flask("sanction_screener")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST'])
def add_list():
    if 'list' not in request.files:
        return "Error: no 'list' file provided", 400
    list_sanctions = request.files['list']
    if list_sanctions.filename == '':
        return "Error: empty filename", 400
    if list_sanctions and allowed_file(list_sanctions.filename):
        filename = secure_filename(list_sanctions.filename)
        list_sanctions.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename))
    return "List added successfully!", 200


@app.route('/<list_name>/<search_name>', methods=['GET'])
def screen(list_name, search_name):
    list_path = os.path.join(app.config['UPLOAD_FOLDER'], list_name)
    results = screen_name(search_name, list_path)
    return '\n'.join(map(lambda x: f"{x[1]} {x[0]}", results)), 200


app.run()
