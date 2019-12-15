from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import *
import datetime


# 主页
def index(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
                room = RoomInfo.objects.get(room_num='01')
                sensor_temperature = SensorInfo.objects.get(belongto_type=2, belongto_id=room.id, sensor_type_id=1)
                sensor_humidity = SensorInfo.objects.get(belongto_type=2, belongto_id=room.id, sensor_type_id=2)
                sensor_co2 = SensorInfo.objects.get(belongto_type=2, belongto_id=room.id, sensor_type_id=4)
                data_record_temperature = DataRecord.objects.filter(sensor_num=sensor_temperature.sensor_num).order_by(
                    '-id')[:10]
                data_record_temperature_latest = data_record_temperature[0]
                data_record_humidity = DataRecord.objects.filter(sensor_num=sensor_humidity.sensor_num).order_by('-id')[
                                       :10]
                data_record_humidity_latest = data_record_humidity[0]
                data_record_co2 = DataRecord.objects.filter(sensor_num=sensor_co2.sensor_num).order_by('-id')[:10]
                data_record_co2_latest = data_record_co2[0]
            except Exception as e:
                print(e)
            content = {
                'active_main_menu': '主页',
                'active_submenu': '水培温室',
                'room': room,
                'data_record_temperature': data_record_temperature,
                'data_record_temperature_latest': data_record_temperature_latest,
                'data_record_humidity': data_record_humidity,
                'data_record_humidity_latest': data_record_humidity_latest,
                'data_record_co2': data_record_co2,
                'data_record_co2_latest': data_record_co2_latest,
            }
            return render(request, 'green/index.html', content)
        if request.method == 'POST':
            room_num = request.POST.get('room_num')
            try:
                room = RoomInfo.objects.get(room_num=room_num)
                sensor_temperature = SensorInfo.objects.get(belongto_type=2, belongto_id=room.id, sensor_type_id=1)
                sensor_humidity = SensorInfo.objects.get(belongto_type=2, belongto_id=room.id, sensor_type_id=2)
                sensor_co2 = SensorInfo.objects.get(belongto_type=2, belongto_id=room.id, sensor_type_id=4)
                data_record_temperature = DataRecord.objects.filter(sensor_num=sensor_temperature.sensor_num).order_by(
                    '-id')[:10]
                data_record_temperature_latest = data_record_temperature[0]
                data_record_humidity = DataRecord.objects.filter(sensor_num=sensor_humidity.sensor_num).order_by('-id')[
                                       :10]
                data_record_humidity_latest = data_record_humidity[0]
                data_record_co2 = DataRecord.objects.filter(sensor_num=sensor_co2.sensor_num).order_by('-id')[:10]
                data_record_co2_latest = data_record_co2[0]
            except Exception as e:
                print(e)
            active_submenu = ""
            if room_num == '01':
                active_submenu = '水培温室'
            else:
                active_submenu = '基质培温室'
            content = {
                'active_main_menu': '主页',
                'active_submenu': active_submenu,
                'room': room,
                'data_record_temperature': data_record_temperature,
                'data_record_temperature_latest': data_record_temperature_latest,
                'data_record_humidity': data_record_humidity,
                'data_record_humidity_latest': data_record_humidity_latest,
                'data_record_co2': data_record_co2,
                'data_record_co2_latest': data_record_co2_latest,
            }
            return render(request, 'green/index.html', content)
    return render(request, 'green/login.html')


# 登录
def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('green:index'))
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
