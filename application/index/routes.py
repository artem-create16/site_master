import os

from flask import Blueprint, render_template, request, send_from_directory
import application.index.controller as controller
from application.index.form import IndexForm
template_dir = os.path.abspath('../templates')
index_blueprint = Blueprint('index', __name__, template_folder=template_dir)


@index_blueprint.route('/')
def index():
    form = IndexForm()
    return render_template('index.html', title='Master', form=form)


@index_blueprint.route('/', methods=["POST", "GET"])
def requisition(*args):
    return controller.requisition(*args)


@index_blueprint.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)
