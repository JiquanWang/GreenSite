from django.urls import path
from . import views

app_name = 'relays'

urlpatterns = [
    path('', views.get_relays_list, name='get_relays_list'),
]