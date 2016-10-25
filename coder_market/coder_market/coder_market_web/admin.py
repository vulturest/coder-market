from django.contrib import admin

# Register your models here.
from models import *
admin.site.register(publisher)
admin.site.register(receiver)
admin.site.register(project)
admin.site.register(UserProfile)