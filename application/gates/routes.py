import os

from flask import Blueprint

import application.gates.controller as controller
from application import talisman
from application.helper.utils import requisition as helper_requisition

template_dir = os.path.abspath('../templates')
gates = Blueprint('gates', __name__, template_folder=template_dir)


@gates.route('/vorota')
@talisman()
def main_gates():
    return controller.main_gates()


# DONT USE
@gates.route('/vorota/promyshlennye-vorota')
@talisman()
def show_gates_prom():
    return controller.show_gates_prom()


@gates.route('/vorota/sectionnye-vorota', methods=["POST", "GET"])
@talisman()
def show_gates_sectionnye():
    return controller.show_gates_sectionnye()


# DONT USE


@gates.route('/vorota/otkatnye-vorota')
@talisman()
def show_gates_otkatnye():
    return controller.show_gates_otkatnye()


@gates.route('/vorota/otkatnye-vorota', methods=["POST", "GET"])
def requisition_otkatnye(*args):
    return helper_requisition(redirect_url='gates.show_gates_otkatnye', link='otkatnye-vorota', *args)


@gates.route('/vorota/raspashnye-vorota')
@talisman()
def show_gates_raspashnye():
    return controller.show_gates_raspashnye()


@gates.route('/vorota/raspashnye-vorota', methods=["POST", "GET"])
def requisition_raspashnye(*args):
    return helper_requisition(redirect_url='gates.show_gates_raspashnye', link='raspashnye-vorota', *args)
