from django.urls import path
from . import views

app_name = 'rules'
urlpatterns = [
    path('', views.get_rules_list, name='get_rules_list'),
    path('add_new_rule/', views.add_new_rule, name='add_new_rule'),
    path('modify_the_rule/<int:rule_id>/', views.modify_the_rule, name='modify_the_rule'),
    path('delete_the_rule/<int:rule_id>/', views.delete_the_rule, name='delete_the_rule'),
    path('adapt_the_rule/<int:rule_id>/', views.adapt_the_rule, name='adapt_the_rule'),
]
