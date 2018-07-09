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
    g = models.ForeignKey(Grade)

    class Meta:
        db_table = 'student'
