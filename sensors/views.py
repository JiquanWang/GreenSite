from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from green.models import SensorInfo, SensorType, RoomInfo, FlowerShelf, DataRecord
from django.urls import reverse, reverse_lazy
import time
# Create your views here.


def get_sensors_list(request):
    if request.user.is_authenticated:
        sensors_list = SensorInfo.objects.all()
        sensor_types_list = SensorType.objects.all()
        rooms = RoomInfo.objects.all()
        shelves = FlowerShelf.objects.all()
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器列表',
            'sensors_list': sensors_list,
            'sensor_types': sensor_types_list,
            'rooms': rooms,
            'shelves': shelves,
        }
        return render(request, 'sensors/sensors_list.html', content)


def sensor_types(request):
    if request.user.is_authenticated:
        sensor_types_list = SensorType.objects.all()
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器类型',
            'sensor_types': sensor_types_list,
        }
        return render(request, 'sensors/sensor_types.html', content)


def add_sensor_type(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            content = {
                'active_main_menu': '传感器',
                'active_submenu': '添加新的传感器类型',
            }
            return render(request, 'sensors/add_sensor_type.html', content)
        if request.method == 'POST':
            sensor_type = request.POST.get('sensor_type')
            sensor_type_unit = request.POST.get('sensor_type_unit')
            try:
                new_sensor_type = SensorType(sensor_type=sensor_type, sensor_type_unit=sensor_type_unit)
                new_sensor_type.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('sensors:sensor_types'))


def add_new_sensor(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            sensor_types_list = SensorType.objects.all()
            rooms = RoomInfo.objects.all()
            shelves = FlowerShelf.objects.all()
            content = {
                'active_main_menu': '传感器',
                'active_submenu': '添加新的传感器',
                'sensor_types': sensor_types_list,
                'rooms': rooms,
                'shelves': shelves,
            }
            return render(request, 'sensors/add_new_sensor.html', content)
        if request.method == 'POST':
            sensor_num = request.POST.get('sensor_num')
            sensor_type_id = request.POST.get('sensor_type_id')
            belongto_type = request.POST.get('belongto_type')
            belongto_id = request.POST.get('belongto_id')
            try:
                sensor = SensorInfo(sensor_num=sensor_num, sensor_type_id=sensor_type_id, belongto_type=belongto_type,
                                    belongto_id=belongto_id, device_index=100, status=0, created_time=int(time.time()))
                sensor.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('sensors:get_sensors_list'))


def modify_the_sensor(request, sensor_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            sensor = SensorInfo.objects.get(id=sensor_id)
            sensor_types_list = SensorType.objects.all()
            rooms = RoomInfo.objects.all()
            shelves = FlowerShelf.objects.all()
            content = {
                'active_main_menu': '传感器',
                'active_submenu': '修改传感器信息',
                'sensor_types': sensor_types_list,
                'rooms': rooms,
                'shelves': shelves,
                'sensor': sensor,
            }
            return render(request, 'sensors/modify_the_sensor.html', content)
        if request.method == 'POST':
            try:
                sensor = SensorInfo.objects.get(id=sensor_id)
                sensor.sensor_num = request.POST.get('sensor_num')
                sensor.sensor_type_id = request.POST.get('sensor_type_id')
                sensor.belongto_type = request.POST.get('belongto_type')
                sensor.belongto_id = request.POST.get('belongto_id')
                sensor.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect(reverse('sensors:get_sensors_list'))


def delete_the_sensor(request, sensor_id):
    if request.user.is_authenticated:
        try:
            sensor = SensorInfo.objects.get(id=sensor_id)
            sensor.delete()
        except Exception as e:
            print(e)
        return HttpResponseRedirect(reverse('sensors:get_sensors_list'))


def sensor_data(request, sensor_id):
    if request.user.is_authenticated:
        try:
            sensor = SensorInfo.objects.get(id=sensor_id)
            sensor_type = SensorType.objects.get(id=sensor.sensor_type_id)
            data_record = DataRecord.objects.filter(sensor_num=sensor.sensor_num).order_by('-id')[:20]
        except Exception as e:
            print(e)
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器数据',
            'sensor': sensor,
            'sensor_type': sensor_type,
            'data_record': data_record,
        }
        return render(request, 'sensors/sensor_data.html', content)
