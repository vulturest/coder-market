from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from models import *
# Create your views here.

def helloworld(request):
    context = {}
    context['label'] = "hello world"
    return render(request,'helloworld.html',context)

def register(request):
    if request.method == 'POST':
        reg = User()
        reg.username=request.POST['register_username']
        reg.password=request.POST['register_password']
        reg.save()
        return HttpResponse("run!")
    return render(request,'register.html',{})