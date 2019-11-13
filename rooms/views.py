from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import RoomInfo, QuanShi
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
