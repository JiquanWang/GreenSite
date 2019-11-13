from django.urls import path
from . import views

app_name = 'sensors'

urlpatterns = [
    path('', views.get_sensors_list, name='get_sensors_list'),
]