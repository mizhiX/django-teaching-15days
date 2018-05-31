from django.db import models


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'day51_student'


class StudentInfo(models.Model):

    i_addr = models.CharField(max_length=30)
    i_image = models.ImageField(upload_to='upload', null=True)
    s = models.OneToOneField(Student)

    class Meta:
        db_table = 'day51_Student_info'


class Visit(models.Model):

    v_url = models.CharField(max_length=30)
    v_times = models.IntegerField()

    class Meta:
        db_table = 'day7_visit'
