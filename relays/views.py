from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import RelayInfo, RoomInfo, FlowerShelf
import time
# Create your views here.


def get_relays_list(request):
    if request.user.is_authenticated:
        relays_list = RelayInfo.objects.all()
        content = {
            'active_main_menu': '控制器',
            'active_submenu': '控制器列表',
            'relays_list': relays_list,
        }
        return render(request, 'relays/relays_list.html', content)


def add_new_relay(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            rooms = RoomInfo.objects.all()
            shelves = FlowerShelf.objects.all()
            content = {
                'active_main_menu': '控制器',
                'active_submenu': '添加新的控制器',
                'rooms': rooms,
                'shelves': shelves,
            }
            return render(request, 'relays/add_new_relay.html', content)
        if request.method == 'POST':
            relay_num = request.POST.get('relay_num')
            relay_name = request.POST.get('relay_name')
            device_type = request.POST.get('device_type')
            status = request.POST.get('status')
            belongto_type = request.POST.get('belongto_type')
            belongto_id = request.POST.get('belongto_id')
            try:
                relay = RelayInfo(relay_num=relay_num, relay_name=relay_name, device_type=device_type,
                                  status=status, belongto_type=belongto_type, belongto_id=belongto_id,
                                  is_online=0, refresh_time=0, created_time=int(time.time()),
                                  relay_type_id=relay_num[:2])
                relay.save()
            except Exception as e:
                print(e)

            return HttpResponseRedirect(reverse('relays:get_relays_list'))
