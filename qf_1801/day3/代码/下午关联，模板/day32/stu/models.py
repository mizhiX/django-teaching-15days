from django.db import models

from grade.models import Grade

class Student(models.Model):
    stu_name = models.CharField(max_length=10)
    stu_sex = models.BooleanField()
    stu_birth = models.DateField()
    stu_create_time = models.DateTimeField(auto_now_add=True)
    stu_operate_time = models.DateTimeField(auto_now=True)
    stu_yuwen = models.DecimalField(max_digits=3, decimal_places=1)
    stu_shuxue = models.DecimalField(max_digits=3, decimal_places=1)
    g = models.ForeignKey(Grade, null=True)

    class Meta:
        db_table = 'stu'

class StudentInfo(models.Model):

    stu_addr = models.CharField(max_length=30)
    stu_age = models.IntegerField()
    stu = models.OneToOneField(Student,
                               on_delete=models.CASCADE,
                               related_name='stu_info')

    class Meta:
        db_table = 'stu_info'

class GoodsUser(models.Model):
    u_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'good_user'

class Goods(models.Model):
    g_name = models.CharField(max_length=10)
    g_user = models.ManyToManyField(GoodsUser)

    class Meta:
        db_table = 'goods'

