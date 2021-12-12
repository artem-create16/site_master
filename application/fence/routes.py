import os

from flask import Blueprint

import application.fence.controller as controller
from application import talisman
from application.helper.utils import requisition as helper_requisition

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


@fence.route('/zabory/profnastil', methods=["POST", "GET"])
def requisition_profnastil(*args):
    return helper_requisition(redirect_url='fence.show_fence_profnastil', link='zabory/profnastil', *args)


@fence.route('/zabory/evroshtaketnik')
@talisman()
def show_fence_evroshtaketnik():
    return controller.show_fence_evroshtaketnik()


@fence.route('/zabory/evroshtaketnik', methods=["POST", "GET"])
def requisition_evroshtaketnik(*args):
    return helper_requisition(redirect_url='fence.show_fence_evroshtaketnik', link='zabory/evroshtaketnik', *args)


@fence.route('/zabory/rabitz')
@talisman()
def show_fence_rabitz():
    return controller.show_fence_rabitz()


@fence.route('/zabory/rabitz', methods=["POST", "GET"])
def requisition_rabitz(*args):
    return helper_requisition(redirect_url='fence.show_fence_rabitz', link='zabory/rabitz', *args)


@fence.route('/zabory/3d')
@talisman()
def show_fence_3d():
    return controller.show_fence_3d()


@fence.route('/zabory/3d', methods=["POST", "GET"])
def requisition_3d(*args):
    return helper_requisition(redirect_url='fence.show_fence_3d', link='zabory/3d', *args)

