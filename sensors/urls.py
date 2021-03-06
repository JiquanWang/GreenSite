from django.urls import path
from . import views

app_name = 'sensors'

urlpatterns = [
    path('', views.get_sensors_list, name='get_sensors_list'),
    path('sensor_types/', views.sensor_types, name='sensor_types'),
    path('add_sensor_type/', views.add_sensor_type, name='add_sensor_type'),
    path('add_new_sensor/', views.add_new_sensor, name='add_new_sensor'),
    path('modify_the_sensor/<int:sensor_id>/', views.modify_the_sensor, name='modify_the_sensor'),
    path('delete_the_sensor/<int:sensor_id>/', views.delete_the_sensor, name='delete_the_sensor'),
    path('sensor_data/<int:sensor_id>/', views.sensor_data, name='sensor_data'),
]