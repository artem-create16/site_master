import os

from flask import Blueprint, render_template, send_from_directory

from application.helper.utils import requisition as helper_requisition
from application import talisman
from application.index.form import IndexForm

template_dir = os.path.abspath('../templates')
index_blueprint = Blueprint('index', __name__, template_folder=template_dir)


@index_blueprint.route('/')
@talisman()
def index():
    form = IndexForm()
    return render_template('index.html', form=form)


@index_blueprint.route('/', methods=["POST", "GET"])
def requisition(*args):
    return helper_requisition(redirect_url='index.index', link='Главная страница', *args)


@index_blueprint.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@index_blueprint.route('/polzovatelskoe-soglashenie')
@talisman()
def assign():
    return render_template('assign.html')
