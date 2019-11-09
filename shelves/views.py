from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,Http404,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from .models import FlowerShelf
import datetime
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
