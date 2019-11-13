from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
import datetime


# 主页
def index(request):
    if request.user.is_authenticated:
        content = {
            'active_main_menu': 'Home',
            'active_submenu': None,
        }
        return render(request, 'green/index.html', content)
    return render(request, 'green/login.html')


# 登录
def login(request):
    if request.user.is_authenticated:
        return render(request, 'green/index.html')
    if request.method == 'GET':
        return render(request, 'green/login.html')
    state = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('green:index'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'state': state,
        'user': None,
    }
    return render(request, 'green/login.html', content)


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'green/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username=username, password=password, email=email)
        return render(request, 'green/login.html')


# 登出
def logout(request):
    auth.logout(request)
    return render(request, 'green/login.html')


# 个人信息
def userinfo(request):
    if request.user.is_authenticated:
        content = {
            'active_main_menu': '系统设置',
            'active_submenu': '个人信息',
        }
        return render(request, 'green/userinfo.html', content)
    else:
        raise Http404("Please sign in!")
