from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from green.models import RelayInfo, RoomInfo, FlowerShelf, ControlData
import time, math
# Create your views here.


def get_relays_list(request):
    if request.user.is_authenticated:
        relays_list = RelayInfo.objects.all()
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


def modify_the_relay(request, relay_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            rooms = RoomInfo.objects.all()
            shelves = FlowerShelf.objects.all()
            relay = RelayInfo.objects.get(id=relay_id)
            content = {
                'active_main_menu': '控制器',
                'active_submenu': '修改控制器信息',
                'rooms': rooms,
                'shelves': shelves,
                'relay': relay,
            }
            return render(request, 'relays/modify_the_relay.html', content)
        if request.method == 'POST':
            try:
                relay = RelayInfo.objects.get(id=relay_id)
                last_status = relay.status
                relay.relay_num = request.POST.get('relay_num')
                relay.relay_name = request.POST.get('relay_name')
                relay.device_type = request.POST.get('device_type')
                relay.status = request.POST.get('status')
                relay.belongto_type = request.POST.get('belongto_type')
                relay.belongto_id = request.POST.get('belongto_id')
                relay.save()
                if math.fabs(last_status-float(relay.status)) > 1e-5:
                    control_data = ControlData(relay_num=relay.relay_num, relay_name=relay.relay_name,
                                               belongto_type=relay.belongto_type, belongto_id=relay.belongto_id,
                                               relay_type=relay.device_type, relay_value=relay.status,
                                               collect_time=int(time.time()))
                    control_data.save()
            except Exception as e:
                print(e)

            return HttpResponseRedirect(reverse('relays:get_relays_list'))


def delete_the_relay(request, relay_id):
    if request.user.is_authenticated:
        try:
            relay = RelayInfo.objects.get(id=relay_id)
            relay.delete()
        except Exception as e:
            print(e)
        return HttpResponseRedirect(reverse('relays:get_relays_list'))


def adapt_the_relay(request, relay_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            try:
                relay = RelayInfo.objects.get(id=relay_id)
                if relay.status == 1:
                    relay.status = 2
                else:
                    relay.status = 1
                relay.save()
                control_data = ControlData(relay_num=relay.relay_num, relay_name=relay.relay_name,
                                           belongto_type=relay.belongto_type, belongto_id=relay.belongto_id,
                                           relay_type=relay.device_type, relay_value=relay.status,
                                           collect_time=int(time.time()))
                control_data.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('relays:get_relays_list'))
        if request.method == 'POST':
            try:
                relay = RelayInfo.objects.get(id=relay_id)
                last_status = relay.status
                relay.status = request.POST.get('status')
                relay.save()
                if math.fabs(last_status-float(relay.status)) > 1e-5:
                    control_data = ControlData(relay_num=relay.relay_num, relay_name=relay.relay_name,
                                               belongto_type=relay.belongto_type, belongto_id=relay.belongto_id,
                                               relay_type=relay.device_type, relay_value=relay.status,
                                               collect_time=int(time.time()))
                    control_data.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('relays:get_relays_list'))
