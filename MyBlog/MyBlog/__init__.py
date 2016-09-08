# -*- coding:utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment


def create_app(config_name):
    app = Flask(__name__)
    moment = Moment(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app