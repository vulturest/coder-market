from django.contrib import admin
from django.contrib.auth.models import User

from models import publisher,receiver,project,UserProfile

# Register your models here.
admin.site.register(publisher)
admin.site.register(receiver)
admin.site.register(project)
admin.site.register(User, UserProfile)
