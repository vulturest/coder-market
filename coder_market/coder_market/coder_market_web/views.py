#coding=utf8
import django.contrib.auth
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

from models import *


# Create your views here.

def helloworld(request):
    context = {}
    context['label'] = request.user.username
    return render(request, 'helloworld.html', context)


def register(request):
    if request.method == 'POST':
        reg = User()
        reg.username = request.POST['register_username']
        reg.set_password(request.POST['register_password'])
        reg.save()
        pro = UserProfile(user_id=reg.id)
        pro.identity = request.POST['register_identity']
        pro.save()
        return HttpResponseRedirect('/login')
    return render(request, 'register.html', {})


def login(request):
    if request.method == "POST":
        print request.POST['login_username'], request.POST['login_password']
        user = django.contrib.auth.authenticate(username=request.POST['login_username'],
                                                password=request.POST['login_password'])
        if user is not None:
            django.contrib.auth.login(request, user)
            return HttpResponseRedirect('/hello')
        else:
            return render(request,'login.html',{'error':'你输入了错误的账号或者密码'})
    return render(request, 'login.html', {})


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponse("success to logout")
