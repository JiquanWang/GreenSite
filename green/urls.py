from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /green/
    path('', views.index, name='index')
]
