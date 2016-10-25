from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from models import publisher,receiver,project,UserProfile
admin.site.register(publisher)
admin.site.register(receiver)
admin.site.register(project)
admin.site.register(User,UserProfile)
