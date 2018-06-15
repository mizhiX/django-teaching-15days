
from datetime import datetime


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    s_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    s_name = db.Column(db.String(16), unique=True)
    s_age = db.Column(db.Integer, default=16)
    grades = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)

    # __tablename__ = 'student'

    # def __init__(self, name, age):
    #     self.s_name = name
    #     self.s_age = age

    def to_dict(self):
        return {
            's_name': self.s_name
        }


class Grade(db.Model):

    g_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    g_name = db.Column(db.String(16), unique=True, nullable=False)
    g_desc = db.Column(db.String(30), nullable=True)
    g_create_time = db.Column(db.DateTime, default=datetime.now)
    students = db.relationship('Student', backref='grade', lazy='dynamic')

    __tablename__ = 'grade'


sc = db.Table('sc',
              db.Column('s_id', db.Integer, db.ForeignKey('student.s_id'), primary_key=True),
              db.Column('c_id', db.Integer, db.ForeignKey('course.c_id'), primary_key=True),
              )


class Course(db.Model):

    c_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(16), unique=True)
    c_create_time = db.Column(db.DateTime, default=datetime.now)
    students = db.relationship('Student',
                               secondary=sc,
                               backref='course')

    __tablename__ = 'course'

    def to_dict(self):
        return {
            'c_id': self.c_id,
            'c_name': self.c_name,
            'c_create_time': self.c_create_time.strftime('%Y-%m-%d'),
            'students': [stu.to_dict() for stu in self.students]
        }


class User(db.Model):

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(200))
    create_time = db.Column(db.DateTime, default=datetime.now)

    __tablename__ = 'user'

    def __init__(self, name, pwd):
        self.username = name
        self.password = pwd

    def save(self):
        db.session.add(self)
        db.session.commit()
