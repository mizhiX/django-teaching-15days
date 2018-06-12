
import os

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import redis

from App.hellow_views import hello_blueprint
from App.user_views import user_blueprint


db = SQLAlchemy()


def create_app():

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    static_dir = os.path.join(BASE_DIR, 'static')
    templates_dir = os.path.join(BASE_DIR, 'templates')

    app = Flask(__name__,
                static_folder=static_dir,
                template_folder=templates_dir)

    app.register_blueprint(blueprint=hello_blueprint, url_prefix='/hello')
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

    app.config['SECRET_KEY'] = 'secret_key'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = redis.Redis(host='127.0.0.1', port=6379)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/helloFlask2'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 第一种方式
    # se = Session()
    # se.init_app(app=app)
    # 第二种方式
    Session(app=app)

    db.init_app(app=app)

    return app

