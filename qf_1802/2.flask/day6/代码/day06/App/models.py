
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(object):
    # 定义基础的模型
    create_time = db.Column(db.DATETIME, default=datetime.now())
    update_time = db.Column(db.DATETIME, default=datetime.now(),
                            onupdate=datetime.now())

    def add_update(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class User(BaseModel, db.Model):

    __tablename__ = 'ihome_user'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(11), unique=True)
    pwd_hash = db.Column(db.String(200))
    name = db.Column(db.String(30), unique=True)
    avatar = db.Column(db.String(100))  # 头像
    id_name = db.Column(db.String(30))  # 实名认证的姓名
    id_card = db.Column(db.String(18), unique=True)  # 实名认证的身份证号码

    # houses=db.relationship('House',backref='user')
    # orders=db.relationship('Order',backref='user')

    #读
    @property
    def password(self):
        return ''
    #写
    @password.setter
    def password(self, pwd):
        self.pwd_hash = generate_password_hash(pwd)

    #对比
    def check_pwd(self, pwd):
        return check_password_hash(self.pwd_hash, pwd)

    def to_auth_dict(self):
        return {
            'id_name': self.id_name,
            'id_card': self.id_card
        }

    def to_basic_dict(self):
        return {
            'id': self.id,
            'avatar': self.avatar if self.avatar else '',
            'name': self.name,
            'phone': self.phone
        }