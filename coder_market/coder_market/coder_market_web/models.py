from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class publisher(models.Model):
    username = models.CharField(max_length=30)
    order_project = models.IntegerField()
    presonal_information = models.CharField(max_length=100)
    accept_information = models.TextField()

    def __unicode__(self):
        return self.username



class receiver(models.Model):
    username = models.CharField(max_length=30)
    get_project = models.IntegerField()
    presonal_information = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    accept_information = models.TextField()
    def __unicode__(self):
        return self.username


class manager(models.Model):
    username = models.CharField(max_length=30)
    manage_project = models.IntegerField()
    presonal_information = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    accept_information = models.TextField()
    def __unicode__(self):
        return self.username


class project(models.Model):
    title = models.CharField(max_length=50)
    project_publisher = models.CharField(max_length=30)
    project_content = models.TextField()
    project_receiver = models.CharField(max_length=100)
    project_manager = models.CharField(max_length=30)
    tag = models.CharField(max_length=50)
    need_receiver_num = models.IntegerField()
    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    # user = models.ForeignKey(User, unique=True, verbose_name='profile')
    user = models.OneToOneField(User, unique=True)
    identity = models.CharField(max_length=15)

    def __unicode__(self):
        return self.identity

admin.site.register(publisher)
admin.site.register(receiver)
admin.site.register(project)
admin.site.register(UserProfile)
