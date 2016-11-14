# coding=utf8
import django.contrib.auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from assistant import *
from models import *


# Create your views here.

def helloworld(request):
    context = {}
    context['label'] = request.user.username
    return render(request, 'helloworld.html', context)


def register(request):
    if request.method == 'POST':
        reg = User()
        if is_vaild_username(request.POST['register_username']) and is_vaild_password(request.POST['register_password']) and is_vaild_email(request.POST['register_email']):
            reg.username = request.POST['register_username']
            reg.set_password(request.POST['register_password'])
            reg.email = request.POST['register_email']
            reg.save()
            pro = UserProfile(user_id=reg.id)
            pro.identity = request.POST['checked']
            pro.save()
        else:
            return render(request, 'register.html', {'error':'请合法输入'})
        if request.POST['checked'] == 'customer':
            p = publisher()
            p.username = request.POST['register_username']
            p.presonal_information = request.POST['register_information']
            p.save()
        elif request.POST['checked'] == 'program':
            p = receiver()
            p.username = request.POST['register_username']
            p.presonal_information = request.POST['register_information']
            p.tag = request.POST['register_tag']
            p.save()
        elif request.POST['checked'] == 'manager':
            p = manager()
            p.username = request.POST['register_username']
            p.presonal_information = request.POST['register_information']
            p.tag = request.POST['register_tag']
            p.save()

        return HttpResponseRedirect('/login')
    else:
        return render(request, 'register.html', {})


def login(request):
    if request.method == "POST":
        if is_vaild_username(request.POST['login_username']) and is_vaild_password(request.POST['login_password']):
            user = django.contrib.auth.authenticate(username=request.POST['login_username'],
                                                    password=request.POST['login_password'])
            if user is not None:
                django.contrib.auth.login(request, user)
                return HttpResponseRedirect('/hello')
            else:
                return render(request, 'login.html', {'error': '你输入了错误的账号或者密码'})
        else:
            return render(request, 'login.html', {'error':'请输入合法用户名和密码'})
    return render(request, 'login.html', {})


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponse("success to logout")


def newproject(request):
    if request.method == "POST":
        new_p = project()
        new_p.title = request.POST['project_title']
        new_p.need_receiver_num = request.POST['project_need_num']
        new_p.tag = request.POST['tag'].replace('，',',').split(',')
        new_p.project_content = request.POST['content']
        new_p.project_publisher = request.user.username
        new_p.status = 0  # 待领取状态
        new_p.save()
        return HttpResponseRedirect('/hello')
    else:
        '''
        记得区分身份再渲染模板
        '''
        if not request.user.is_authenticated():
            return render(request, 'login.html', {'error': '请您先登录'})
        else:
            profile = request.user.userprofile
            if profile.identity == 'customer':
                return render(request, 'newproject.html', {})
            else:
                return HttpResponseRedirect('/hello')

def project_view(request):
    if request.method == 'POST':
        pass
    else:
        project_num = int(request.path.split('/')[-1])
        try:
            this_project = project.objects.get(need_receiver_num=project_num)
            if not request.user.is_authenticated():
                content_dict = {'title': this_project.title, 'content': this_project.project_content}
                if this_project.status == 0:
                    content_dict['status']='招聘中'
                elif this_project.status == 1:
                    content_dict['status'] = '已经开始'
                content_dict['publisher'] = this_project.project_publisher
                content_dict['tag'] = ' '.join(this_project.tag)
                return render(request, 'project.html', content_dict)
            elif request.user.username == this_project.project_publisher:
                content_dict = {'title': this_project.title, 'content': this_project.project_content}
                if this_project.status == 0:
                    content_dict['status']='招聘中'
                elif this_project.status == 1:
                    content_dict['status'] = '已经开始'
                content_dict['publisher'] = this_project.project_publisher
                content_dict['tag'] = ' '.join(this_project.tag)
                return render(request, 'project.html', content_dict)
        except project.DoesNotExist:
            return render(request, 'project.html',
                          {'title': '没有相应的项目'})
def homepage(request):
    if request.method == 'POST':
        pass
     else:
        project_num = int(request.path.split('/')[-1])
        try:
            this_project = project.objects.get(need_receiver_num=project_num)
            if not request.user.is_authenticated():
                content_dict = {'title': this_project.title, 'content': this_project.project_content}
                if this_project.status == 0:
                    content_dict['status']='招聘中'
                elif this_project.status == 1:
                    content_dict['status'] = '已经开始'
                content_dict['publisher'] = this_project.project_publisher
                content_dict['tag'] = ' '.join(this_project.tag)
                return render(request, 'project.html', content_dict)
            elif request.user.username == this_project.project_publisher:
                content_dict = {'title': this_project.title, 'content': this_project.project_content}
                if this_project.status == 0:
                    content_dict['status']='招聘中'
                elif this_project.status == 1:
                    content_dict['status'] = '已经开始'
                content_dict['publisher'] = this_project.project_publisher
                content_dict['tag'] = ' '.join(this_project.tag)
                return render(request, 'project.html', content_dict)
        except project.DoesNotExist:
            return render(request, 'project.html',
                          {'title': '没有相应的项目'})