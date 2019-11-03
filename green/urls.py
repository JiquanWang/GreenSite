from django.urls import path
from . import views

app_name = 'green'
urlpatterns = [
    # ex: /green/
    path('', views.index, name='index'),
    # path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register')
]
