
import re
import os

from flask import Blueprint, render_template, request, \
    jsonify, session

from App.models import db, User
from utils import status_code
from utils.setting import UPLOAD_DIR

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/')
def hello():
    return 'hello world'


@user_blueprint.route('/create_db/')
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


@user_blueprint.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')


@user_blueprint.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')


@user_blueprint.route('/profile/', methods=['POST'])
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
