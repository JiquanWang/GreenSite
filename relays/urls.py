from django.urls import path
from . import views

app_name = 'relays'

urlpatterns = [
    path('', views.get_relays_list, name='get_relays_list'),
    path('add_new_relay/', views.add_new_relay, name='add_new_relay'),
    path('modify_the_relay/<int:relay_id>/', views.modify_the_relay, name='modify_the_relay'),
    path('delete_the_relay/<int:relay_id>/', views.delete_the_relay, name='delete_the_relay'),
    path('adapt_the_relay/<int:relay_id>/', views.adapt_the_relay, name='adapt_the_relay'),
]