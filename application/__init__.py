import os
from flask_mail import Mail
from flask import Flask
from dotenv import load_dotenv
from flask_talisman import Talisman

load_dotenv()
mail = Mail()
talisman = Talisman()


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = str(os.getenv("WORK_MAIL"))
    app.config['MAIL_PASSWORD'] = str(os.getenv("WORK_MAIL_PASSWORD"))
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    with app.app_context():
        from application.index.routes import index_blueprint
        from application.calculator.routes import calculator_blueprint
        from application.error.routes import error_blueprint
        from application.roller_shutters.routes import roller_shutters
        from application.fence.routes import fence
        app.register_blueprint(index_blueprint)
        app.register_blueprint(calculator_blueprint)
        app.register_blueprint(error_blueprint)
        app.register_blueprint(roller_shutters)
        app.register_blueprint(fence)

    mail.init_app(app)
    talisman.init_app(app, content_security_policy={})
    return app
