import os

from flask import Flask

from user.stu_views import stu_blueprint
from user.user_views import blue


def create_app():
    # 静态/template目录
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)

    app.register_blueprint(blueprint=blue, url_prefix='/app')
    app.register_blueprint(blueprint=stu_blueprint, url_prefix='/stu')

    return app
