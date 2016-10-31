from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
'''
class user_login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    identity = models.CharField(max_length=15)
'''

'''
class identity(models.Model):
    username = models.ForeignKey(User)
    iden = models.CharField(max_length=10)
'''


class publisher(models.Model):
    username = models.CharField(max_length=30)
    order_project = models.IntegerField()
    presonal_information = models.CharField(max_length=100)
    accept_information = models.TextField()



class receiver(models.Model):
    username = models.CharField(max_length=30)
    get_project = models.IntegerField()
    presonal_information = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    accept_information = models.TextField()


class manager(models.Model):
    username = models.CharField(max_length=30)
    manage_project = models.IntegerField()
    presonal_information = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    accept_information = models.TextField()


class project(models.Model):
    number = models.IntegerField()
    project_publisher = models.CharField(max_length=30)
    project_content = models.TextField()
    project_receiver = models.CharField(max_length=30)
    project_manager = models.CharField(max_length=30)
    tag = models.CharField(max_length=50)


class UserProfile(models.Model):
    # user = models.ForeignKey(User, unique=True, verbose_name='profile')
    user = models.OneToOneField(User, unique=True)
    identity = models.CharField(max_length=15)


admin.site.register(publisher)
admin.site.register(receiver)
admin.site.register(project)
admin.site.register(UserProfile)
