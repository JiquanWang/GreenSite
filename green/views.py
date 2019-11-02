from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy


# 起始
def begin(request):
    return render(request, 'green/login.html')


# 主页
def index(request):
    return render(request, 'green/index.html')


# 登录
def login(request):
    state = None
    if request.method == 'POST':
        username = request.POST.get('Username', '')
        password = request.POST.get('Password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('index')
        else:
            state ='not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'green/login.html', content)


# 登出
def logout(request):
    return render(request, 'green/login.html')
