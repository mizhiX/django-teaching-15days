
from flask import render_template, Blueprint


blue = Blueprint('first', __name__)


@blue.route('/hello/')
def hello():
    # 3/0
    return 'hello world'


@blue.route('/hellohtml/')
def hello_html():
    return render_template('hello.html')


@blue.route('/hello/<name>/')
def hello_person(name):
    return render_template('hello.html', name=name)


@blue.route('/helloint/<int:id>/')
def hello_int(id):
    return render_template('hello.html', id=id)


@blue.route('/hellofloat/<float:float_id>/')
def hello_float(float_id):
    return render_template('hello.html', float_id=float_id)


@blue.route('/hellopath/<path:path>/')
def hello_path(path):
    return render_template('hello.html', path=path)


@blue.route('/hellouuid/<uuid:uuid>/')
def hello_uuid(uuid):
    return render_template('hello.html', uuid=uuid)
