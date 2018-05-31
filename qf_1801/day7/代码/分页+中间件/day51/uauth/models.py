from django.db import models

class Users(models.Model):

    u_name = models.CharField(max_length=10)
    u_password = models.CharField(max_length=255)
    u_ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'day51_users'
