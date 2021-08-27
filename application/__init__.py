import os

from flask import Flask
from application.index.routes import index_blueprint


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    with app.app_context():
        app.register_blueprint(index_blueprint)

    return app
