from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=20)
    g_create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'grade'


class Student(models.Model):
    s_name = models.CharField(max_length=20, null=False, unique=True)
    s_create_time = models.DateTimeField(auto_now_add=True)
    s_operate_time = models.DateTimeField(auto_now=True)
    s_img = models.ImageField(upload_to='upload', null=True)
    g = models.ForeignKey(Grade)
    s_yuwen = models.IntegerField(null=True)
    s_shuxue = models.IntegerField(null=True)
    delete = models.BooleanField(default=False)

    class Meta:
        db_table='student'
    #
    # def __init__(self, name, g):
    #     self.s_name = name
    #     self.g = g

