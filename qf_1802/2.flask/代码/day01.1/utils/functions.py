import os

from flask import Flask
from user.user_views import user_blueprint


def create_app():

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    template_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=template_dir
                )
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

    return app