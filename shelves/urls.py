from django.urls import path
from . import views

app_name = 'shelves'

urlpatterns = [
    path('', views.get_shelves_list, name='get_shelves_list'),
    path('add_new_shelf/', views.add_new_shelf, name='add_new_shelf'),
]
