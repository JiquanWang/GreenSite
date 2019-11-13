from django.shortcuts import render
from green.models import RoomInfo
from green.models import FlowerShelf
from green.models import SensorType
from green.models import SensorInfo
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
