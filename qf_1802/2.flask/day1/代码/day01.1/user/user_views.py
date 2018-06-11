
from flask import Blueprint, render_template, request, \
    make_response, redirect, url_for

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def hello():
    return 'hello'


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        return username


@user_blueprint.route('/user_res/', methods=['GET'])
def get_user_response():
    res = make_response('<h2>大萌妹</h2>', 200)
    return res


@user_blueprint.route('/redirect/')
def user_redirect():
    # return redirect('/user/login/')
    # 初始化蓝图第一个参数，函数名
    return redirect(url_for('user.hello'))




