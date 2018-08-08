'''
Created on 2018年6月26日

@author: nanshenyu
'''
from django.urls import path
from . import views

#start with lab
urlpatterns = [
    #http://localhost:8000/lab/1
    path('', views.lab_list, name = 'lab_list'),
    path('<int:lab_pk>', views.lab_detail, name='lab_detail'),
    path('type/<int:lab_type_pk>',views.lab_with_type, name="lab_with_type"),
    
]
