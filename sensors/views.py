from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from green.models import SensorInfo, SensorType
from django.urls import reverse, reverse_lazy
# Create your views here.


def get_sensors_list(request):
    if request.user.is_authenticated:
        sensors_list = SensorInfo.objects.all()
        content = {
            'active_main_menu': '传感器',
            'active_submenu': '传感器列表',
            'sensors_list': sensors_list,
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
