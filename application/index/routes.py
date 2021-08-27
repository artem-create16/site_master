import os

from flask import Blueprint, render_template, request, send_from_directory

template_dir = os.path.abspath('../templates')
index_blueprint = Blueprint('index', __name__, template_folder=template_dir)


@index_blueprint.route('/')
def index():
    return render_template('index.html', title='Master')


@index_blueprint.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
