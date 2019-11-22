from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import FlowerShelf, RoomInfo, SensorInfo, RelayInfo
import datetime, time
# Create your views here.


def get_shelves_list(request):
    if request.user.is_authenticated:
        shelves_list = FlowerShelf.objects.all()
        content = {
            'active_main_menu': '花架',
            'active_submenu': '花架列表',
            'shelves_list': shelves_list,
        }
        return render(request, 'shelves/shelves_list.html', content)


def add_new_shelf(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            rooms = RoomInfo.objects.all()
            content = {
                'active_main_menu': '花架',
                'active_submenu': '添加新花架',
                'rooms': rooms,
            }
            return render(request, 'shelves/add_new_shelf.html', content)
        if request.method == 'POST':
            name = request.POST.get('name')
            room_id = request.POST.get('room_id')
            try:
                shelf = FlowerShelf(name=name, room_id=room_id, status=0, created_time=int(time.time()))
                shelf.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('shelves:get_shelves_list'))


def modify_the_shelf(request, shelf_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            shelf = FlowerShelf.objects.get(id=shelf_id)
            rooms = RoomInfo.objects.all()
            content = {
                'active_main_menu': '花架',
                'active_submenu': '修改花架信息',
                'rooms': rooms,
                'shelf': shelf,
            }
            return render(request, 'shelves/modify_the_shelf.html', content)
        if request.method == 'POST':
            try:
                shelf = FlowerShelf.objects.get(id=shelf_id)
                shelf.name = request.POST.get('name')
                shelf.room_id = request.POST.get('room_id')
                shelf.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('shelves:get_shelves_list'))


def get_shelf_sensors(request, shelf_id):
    if request.user.is_authenticated:
        sensors_list = SensorInfo.objects.filter(belongto_type=1, belongto_id=shelf_id)
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器列表',
            'sensors_list': sensors_list,
        }
        return render(request, 'sensors/sensors_list.html', content)


def get_shelf_relays(request, shelf_id):
    if request.user.is_authenticated:
        relays_list = RelayInfo.objects.filter(belongto_type=1, belongto_id=shelf_id)
        content = {
            'active_main_menu': '控制器',
            'active_submenu': '控制器列表',
            'relays_list': relays_list,
        }
        return render(request, 'relays/relays_list.html', content)
