from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import RoomInfo, QuanShi, SensorInfo, FlowerShelf, RelayInfo
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
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器列表',
            'sensors_list': sensors_list,
        }
        return render(request, 'sensors/sensors_list.html', content)


def get_room_relays(request, room_id):
    if request.user.is_authenticated:
        relays_list = RelayInfo.objects.filter(belongto_type=2, belongto_id=room_id)
        content = {
            'active_main_menu': '控制器',
            'active_submenu': '控制器列表',
            'relays_list': relays_list,
        }
        return render(request, 'relays/relays_list.html', content)
