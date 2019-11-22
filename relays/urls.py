from django.urls import path
from . import views

app_name = 'relays'

urlpatterns = [
    path('', views.get_relays_list, name='get_relays_list'),
    path('add_new_relay/', views.add_new_relay, name='add_new_relay'),
]