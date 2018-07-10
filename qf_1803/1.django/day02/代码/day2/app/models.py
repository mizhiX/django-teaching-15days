from django.db import models


class Grade(models.Model):

    g_name = models.CharField(max_length=10, unique=True)
    g_crate_time = models.DateTimeField(auto_now_add=True)
    g_modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_sex = models.BooleanField(default=1)
    g = models.ForeignKey(Grade)

    class Meta:
        db_table = 'student'


class MyUser(models.Model):

    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=255, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=0)
    ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'my_user'
