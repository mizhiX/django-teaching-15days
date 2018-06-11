
from flask import Blueprint

stu_blueprint = Blueprint('stu', __name__)


@stu_blueprint.route('/')
def scores():

    return '分数'
