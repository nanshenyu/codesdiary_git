'''
Created on 2018年6月26日

@author: nanshenyu
'''
from django.urls import path
from . import views

#start with diary
urlpatterns = [
    #http://localhost:8000/diary/1
    path('', views.diary_list, name = 'diary_list'),
    path('<int:diary_pk>', views.diary_detail, name='diary_detail'),
    path('type/<int:diary_type_pk>',views.diary_with_type, name="diary_with_type"),
    
]
