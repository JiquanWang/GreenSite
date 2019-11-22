from django.urls import path
from . import views

app_name = 'rooms'
urlpatterns = [
    path('', views.get_rooms_list, name='get_rooms_list'),
    path('add_new_room/', views.add_new_room, name='add_new_room'),
    path('modify_the_room/<int:room_id>/', views.modify_the_room, name='modify_the_room'),
    path('get_room_shelves/<int:room_id>/', views.get_room_shelves, name='get_room_shelves'),
    path('get_room_sensors/<int:room_id>/', views.get_room_sensors, name='get_room_sensors'),
    path('get_room_relays/<int:room_id>/', views.get_room_relays, name='get_room_relays'),
]
