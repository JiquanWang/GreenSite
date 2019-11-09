from django.urls import path
from . import views

app_name = 'shelves'

urlpatterns = [
    path('', views.get_shelves_list, name='get_shelves_list'),
]