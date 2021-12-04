import os
from application import talisman
from flask import Blueprint, render_template, request, send_from_directory
import application.index.controller as controller
from application.index.form import IndexForm

template_dir = os.path.abspath('../templates')
index_blueprint = Blueprint('index', __name__, template_folder=template_dir)


def main_fence():
    return render_template('fence/main_page.html')


def show_fence_profnastil():
    form = IndexForm()
    return render_template('fence/profnastil.html', form=form)


def show_fence_evroshtaketnik():
    form = IndexForm()
    return render_template('fence/euroshtaketnik.html', form=form)


def show_fence_rabitz():
    form = IndexForm()
    return render_template('fence/rabitz.html', form=form)


def show_fence_3d():
    form = IndexForm()
    return render_template('fence/panel-3d.html', form=form)



