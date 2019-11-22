from django.urls import path
from . import views

app_name = 'shelves'

urlpatterns = [
    path('', views.get_shelves_list, name='get_shelves_list'),
    path('add_new_shelf/', views.add_new_shelf, name='add_new_shelf'),
    path('modify_the_shelf/<int:shelf_id>/', views.modify_the_shelf, name='modify_the_shelf'),
    path('get_shelf_sensors/<int:shelf_id>/', views.get_shelf_sensors, name='get_shelf_sensors'),
    path('get_shelf_relays/<int:shelf_id>/', views.get_shelf_relays, name='get_shelf_relays'),
]
