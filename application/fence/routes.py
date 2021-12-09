import os

from flask import Blueprint

import application.fence.controller as controller
from application import talisman

template_dir = os.path.abspath('../templates')
fence = Blueprint('fence', __name__, template_folder=template_dir)


@fence.route('/zabory')
@talisman()
def main_fence():
    return controller.main_fence()


@fence.route('/zabory/profnastil')
@talisman()
def show_fence_profnastil():
    return controller.show_fence_profnastil()


@fence.route('/zabory/evroshtaketnik')
@talisman()
def show_fence_evroshtaketnik():
    return controller.show_fence_evroshtaketnik()


@fence.route('/zabory/rabitz')
@talisman()
def show_fence_rabitz():
    return controller.show_fence_rabitz()

@fence.route('/zabory/3d')
@talisman()
def show_fence_3d():
    return controller.show_fence_3d()

