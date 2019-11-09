from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.get_rooms_list, name='get_rooms_list'),
]