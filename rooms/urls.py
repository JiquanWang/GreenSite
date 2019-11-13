from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.get_rooms_list, name='get_rooms_list'),
    path('add_new_room/', views.add_new_room, name='add_new_room'),
]
