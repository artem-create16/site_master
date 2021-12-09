import os

from flask import Blueprint

import application.gates.controller as controller
from application import talisman

template_dir = os.path.abspath('../templates')
gates = Blueprint('gates', __name__, template_folder=template_dir)


@gates.route('/vorota')
@talisman()
def main_gates():
    return controller.main_gates()


@gates.route('/vorota/promyshlennye-vorota')
@talisman()
def show_gates_prom():
    return controller.show_gates_prom()


@gates.route('/vorota/sectionnye-vorota')
@talisman()
def show_gates_sectionnye():
    return controller.show_gates_sectionnye()


@gates.route('/vorota/otkatnye-vorota')
@talisman()
def show_gates_otkatnye():
    return controller.show_gates_otkatnye()


@gates.route('/vorota/raspashnye-vorota')
@talisman()
def show_gates_raspashnye():
    return controller.show_gates_raspashnye()
