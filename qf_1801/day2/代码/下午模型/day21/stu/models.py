from django.db import models

# Create your models here.

class Student(models.Model):
    # stu_id = models.AutoField(primary_key=True)
    stu_name = models.CharField(max_length=6, unique=True)
    stu_sex = models.BooleanField(default=0)
    stu_birth = models.DateField()
    stu_delete = models.BooleanField(default=0)
    stu_create_time = models.DateField(auto_now_add=True)
    stu_operate_time = models.DateField(auto_now=True)
    stu_tel = models.CharField(max_length=11)
    stu_yuwen = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    stu_shuxue = models.DecimalField(max_digits=3, decimal_places=1, default=0)


    class Meta:
        db_table = 'stu'
