from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import RoomInfo
import datetime
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
