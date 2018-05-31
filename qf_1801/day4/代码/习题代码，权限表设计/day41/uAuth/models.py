from django.db import models


class Users(models.Model):
    u_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'dy4_user'


class Permission(models.Model):
    p_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'dy4_per'


class Role(models.Model):
    r_name = models.CharField(max_length=10)
    u = models.OneToOneField(Users)
    p = models.ManyToManyField(Permission)

    class Meta:
        db_table = 'dy4_role'
