from django.db import models

# Create your models here.

class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_age = models.IntegerField()
    g_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'student'
