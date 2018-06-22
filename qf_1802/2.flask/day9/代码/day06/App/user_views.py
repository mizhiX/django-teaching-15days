
import re
import os

from flask import Blueprint, render_template, request, \
    jsonify, session, redirect, url_for

from App.models import db, User
from utils import status_code
from utils.setting import UPLOAD_DIR
from utils.functions import is_login

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def hello():
    return 'hello world'


@user_blueprint.route('/create_db/')
@is_login
def create_db():
    db.create_all()
    return '创建数据库成功'


@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


@user_blueprint.route('/register/', methods=['POST'])
def user_register():

    mobile = request.form.get('mobile')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    # 1. 验证数据完整性
    if not all([mobile, password, password2]):
        return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
    # 2. 验证手机号码的正确性
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)
    # 3. 验证密码
    if password != password2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_IS_NOT_VALID)
    # 4. 保存用户数据
    user = User.query.filter(User.phone==mobile).all()
    if user:
        return jsonify(status_code.USER_REGISTER_MOBILE_EXSITS)
    else:
        user = User()
        user.phone = mobile
        user.password = password
        user.name = mobile
        user.add_update()
        return jsonify(status_code.SUCCESS)


@user_blueprint.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')


@user_blueprint.route('/login/', methods=['POST'])
def user_login():

    mobile = request.form.get('mobile')
    password = request.form.get('password')

    # 1.验证数据完整
    if not all([mobile, password]):
        return jsonify(status_code.USER_REGISTER_DATA_NOT_NULL)
    # 2.验证手机正确性
    if not re.match(r'^1[34578]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)
    # 3.验证用户
    user = User.query.filter(User.phone == mobile).first()
    if user:
        # 校验密码
        if not user.check_pwd(password):
            return jsonify(status_code.USER_LOGIN_PASSWORD_IS_NOT_VALID)
        # 4.验证用户成功
        session['user_id'] = user.id
        return jsonify(status_code.SUCCESS)

    else:
        return jsonify(status_code.USER_LOGIN_USER_NOT_EXSITS)


@user_blueprint.route('/logout/', methods=['GET'])
@is_login
def user_logout():
    session.clear()
    # return redirect(url_for('user.login'))
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('/my/', methods=['GET'])
@is_login
def my():
    return render_template('my.html')


@user_blueprint.route('/profile/', methods=['GET'])
@is_login
def profile():
    return render_template('profile.html')


@user_blueprint.route('/profile/', methods=['PATCH'])
def user_profile():

    file = request.files.get('avatar')
    # 校验上传图片格式的正确性
    if not re.match(r'image/.*', file.mimetype):
        return jsonify(status_code.USER_CHANGE_PROFILE_IMAGES)
    # 保存
    image_path = os.path.join(UPLOAD_DIR, file.filename)
    file.save(image_path)

    user = User.query.get(session['user_id'])
    avatar_path = os.path.join('upload', file.filename)
    user.avatar = avatar_path
    try:
        user.add_update()
    except Exception as e:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)
    return jsonify(code=status_code.OK, image_url=avatar_path)


@user_blueprint.route('/proname/', methods=['PATCH'])
@is_login
def user_proname():
    name = request.form.get('name')
    user = User.query.filter_by(name=name).first()
    if user:
        # 过滤用户名是否存在
        return jsonify(status_code.USER_CHANGE_PRONAME_IS_INVALID)
    else:
        user = User.query.get(session['user_id'])
        user.name = name
        try:
            user.add_update()
        except:
            db.session.rollback()
            return jsonify(status_code.DATABASE_ERROR)
        return jsonify(code=status_code.OK, name=name)


@user_blueprint.route('/user/', methods=['GET'])
@is_login
def user_info():
    user = User.query.get(session['user_id'])
    return jsonify(code=status_code.OK, data=user.to_basic_dict())


@user_blueprint.route('/auth/', methods=['GET'])
def auth():
    return render_template('auth.html')


@user_blueprint.route('/auth/', methods=['PATCH'])
@is_login
def user_auth():
    real_name = request.form.get('real_name')
    id_card = request.form.get('id_card')

    if not all([real_name, id_card]):
        return jsonify(status_code.USER_AUTH_DATA_IS_NOT_NULL)

    if not re.match(r'^[1-9]\d{17}$', id_card):
        return jsonify(status_code.USER_AUTH_ID_CARD_IS_NOT_VALID)

    user = User.query.get(session['user_id'])
    user.id_name = real_name
    user.id_card = id_card
    try:
        user.add_update()
    except:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)
    return jsonify(status_code.SUCCESS)


@user_blueprint.route('/auths/', methods=['GET'])
@is_login
def user_auths():
    user = User.query.get(session['user_id'])
    return jsonify(code=status_code.OK, data=user.to_auth_dict())


