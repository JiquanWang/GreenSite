from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import FlowerShelf, RoomInfo
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
                'active_main_menu:': '花架',
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
