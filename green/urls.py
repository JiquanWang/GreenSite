from django.urls import path
from . import views

app_name = 'green'
urlpatterns = [
    # ex: /green/
    path('', views.begin, name='begin'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
