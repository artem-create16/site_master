import os

from flask import Flask
from application.index.routes import index_blueprint
from application.calculator.routes import calculator_blueprint

def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    with app.app_context():
        app.register_blueprint(index_blueprint)
        app.register_blueprint(calculator_blueprint)

    return app
