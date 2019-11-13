from django.shortcuts import render
from green.models import RoomInfo
from green.models import FlowerShelf
from green.models import RelayInfo
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
