
from flask import Blueprint, render_template, make_response, \
    request, session

from App.models import db, Student

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/setcookie/')
def set_cookie():
    temp = render_template('cookies.html')
    # 服务端创建响应
    res = make_response(temp)
    # 绑定cookie值, set_cookie(key, value, max_age, expires)
    res.set_cookie('ticket', '123123123', max_age=10)

    return res


@user_blueprint.route('/delcookie/')
def del_cookie():
    temp = render_template('cookies.html')
    # 服务端创建响应
    res = make_response(temp)
    # 绑定cookie值, del_cookie(key, value, max_age, expires)
    res.delete_cookie('ticket')

    return res


@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        return render_template('login.html', username=username)


@user_blueprint.route('/scores/', methods=['GET'])
def stu_scores():

    scores = [90, 80, 76, 56, 75, 12]

    content_h2 = '<h2>二班女生们最美</h2>'
    content_h3 = '  <h3>二班女生们最美</h3>  '
    return render_template('scores.html',
                           scores=scores,
                           content_h2=content_h2,
                           content_h3=content_h3)


@user_blueprint.route('/create_db/')
def create_db():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/drop_db/')
def drop_db():
    db.drop_all()
    return '删除成功'


@user_blueprint.route('/create_stu/', methods=['GET'])
def create_stu():
    stu = Student()
    stu.s_name = '张三'
    stu.s_age = '17'

    # 创建数据
    db.session.add(stu)
    db.session.commit()

    return '创建学生成功'


@user_blueprint.route('/select_stu/', methods=['GET'])
def select_stu():
    # stus = Student.query.filter(Student.s_name == '张三').all()
    # stus = Student.query.filter_by(s_name='张三')
    # stus = Student.query.all()
    # Student.query.filter(Student.s_name == '张三').first()
    # 修改
    # stu = Student.query.filter_by(s_name='张三').first()
    # stu.s_name = '李四'
    #
    # db.session.add(stu)
    # db.session.commit()
    # 删除
    stu = Student.query.filter_by(s_name='李四').first()
    db.session.delete(stu)
    db.session.commit()

    # return render_template('students.html', stus=stus)
    return '查询成功'


