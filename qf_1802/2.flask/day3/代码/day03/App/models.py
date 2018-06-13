
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


class Grade(db.Model):

    g_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    g_name = db.Column(db.String(16), unique=True, nullable=False)
    g_desc = db.Column(db.String(30), nullable=True)
    g_create_time = db.Column(db.DateTime, default=datetime.now)
    students = db.relationship('Student', backref='grade', lazy=True)

    __tablename__ = 'grade'
