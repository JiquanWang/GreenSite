from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import *
import datetime, time
# Create your views here.


def get_rooms_list(request):
    if request.user.is_authenticated:
        rooms_list = RoomInfo.objects.all()
        content = {
            'active_main_menu': '温室',
            'active_submenu': '温室列表',
            'rooms_list': rooms_list,
        }
        return render(request, "rooms/rooms_list.html", content)


def add_new_room(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            cities = QuanShi.objects.filter(parent=330000)
            content = {
                'active_main_menu': '温室',
                'active_submenu': '添加新温室',
                'cities': cities,
            }
            return render(request, "rooms/add_new_room.html", content)
        if request.method == 'POST':
            room_num = request.POST.get('room_num')
            room_name = request.POST.get('room_name')
            city = request.POST.get('city')
            area = request.POST.get('area')
            try:
                room = RoomInfo(room_num=room_num, room_name=room_name, city=city, area=area, status=0,
                                created_time=int(time.time()))
                room.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('rooms:get_rooms_list'))


def modify_the_room(request, room_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            room = RoomInfo.objects.get(id=room_id)
            cities = QuanShi.objects.filter(parent=330000)
            content = {
                'active_main_menu': '温室',
                'active_submenu': '修改温室信息',
                'room': room,
                'cities': cities,
            }
            return render(request, "rooms/modify_the_room.html", content)
        if request.method == 'POST':
            try:
                room = RoomInfo.objects.get(id=room_id)
                room.room_num = request.POST.get('room_num')
                room.room_name = request.POST.get('room_name')
                room.city = request.POST.get('city')
                room.area = request.POST.get('area')
                room.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('rooms:get_rooms_list'))


def get_room_shelves(request, room_id):
    if request.user.is_authenticated:
        shelves_list = FlowerShelf.objects.filter(room_id=room_id)
        content = {
            'active_main_menu': '花架',
            'active_submenu': '花架列表',
            'shelves_list': shelves_list,
        }
        return render(request, 'shelves/shelves_list.html', content)


def get_room_sensors(request, room_id):
    if request.user.is_authenticated:
        sensors_list = SensorInfo.objects.filter(belongto_type=2, belongto_id=room_id)
        sensor_type_list = SensorType.objects.all()
        rooms = RoomInfo.objects.all()
        shelves = FlowerShelf.objects.all()
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器列表',
            'sensors_list': sensors_list,
            'sensor_types': sensor_type_list,
            'rooms': rooms,
            'shelves': shelves,
        }
        return render(request, 'sensors/sensors_list.html', content)


def get_room_relays(request, room_id):
    if request.user.is_authenticated:
        relays_list = RelayInfo.objects.filter(belongto_type=2, belongto_id=room_id)
        rooms = RoomInfo.objects.all()
        shelves = FlowerShelf.objects.all()
        content = {
            'active_main_menu': '控制器',
            'active_submenu': '控制器列表',
            'relays_list': relays_list,
            'rooms': rooms,
            'shelves': shelves,
        }
        return render(request, 'relays/relays_list.html', content)


def room_environment(request, room_id):
    if request.user.is_authenticated:
        try:
            sensor_temperature = SensorInfo.objects.get(belongto_type=2, belongto_id=room_id, sensor_type_id=1)
            sensor_humidity = SensorInfo.objects.get(belongto_type=2, belongto_id=room_id, sensor_type_id=2)
            sensor_co2 = SensorInfo.objects.get(belongto_type=2, belongto_id=room_id, sensor_type_id=4)
            data_record_temperature = DataRecord.objects.filter(sensor_num=sensor_temperature.sensor_num).order_by(
                '-id')[:20]
            data_record_humidity = DataRecord.objects.filter(sensor_num=sensor_humidity.sensor_num).order_by('-id')[:20]
            data_record_co2 = DataRecord.objects.filter(sensor_num=sensor_co2.sensor_num).order_by('-id')[:20]
        except Exception as e:
            print(e)
        content = {
            'active_main_menu': '温室',
            'active_submenu': '温室环境',
            'data_record_temperature': data_record_temperature,
            'data_record_humidity': data_record_humidity,
            'data_record_co2': data_record_co2,
        }
        return render(request, 'rooms/room_environment.html', content)

