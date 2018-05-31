from django.db import models


class Grade(models.Model):

    g_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'day42_grade'


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_operate_time = models.DateTimeField(auto_now=True)
    g = models.ForeignKey(Grade)

    class Meta:
        db_table = 'day42_student'
