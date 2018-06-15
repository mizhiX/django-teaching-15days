

from flask_session import Session
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api

from App.models import db

se = Session()
toolbar = DebugToolbarExtension()
api = Api()


def ext_init(app):

    se.init_app(app=app)
    db.init_app(app=app)
    toolbar.init_app(app=app)
    api.init_app(app=app)