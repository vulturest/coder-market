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
        reg.email = request.POST['register_email']
        reg.save()
        pro = UserProfile(user_id=reg.id)
        pro.identity = request.POST['checked']
        pro.save()
        return HttpResponseRedirect('/login')
    return render(request, 'register.html', {})


def login(request):
    if request.method == "POST":
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

def newproject(request):
    if request.method == "POST":
        new_p = project()
        new_p.title = request.POST['project_title']
        new_p.need_receiver_num = request.POST['project_need_num']
        new_p.tag = request.POST['tag']
        new_p.project_content = request.POST['content']
        new_p.save()
        return HttpResponseRedirect('/hello')
    else:
        '''
        记得区分身份再渲染模板
        '''
        if not request.user.is_authenticated():
            return render(request,'login.html',{'error':'请您先登录'})
        else:
            profile = request.user.userprofile
            if profile.identity == 'customer':
                return render(request,'newproject.html',{})
            else:
                return HttpResponseRedirect('/hello')

