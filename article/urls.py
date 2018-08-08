'''
Created on 2018-6-22

@author: nanshenyu
'''
from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list,name = 'article_list'),
    path('<int:article_id>',views.article_detail,name = 'article_detail'),
    
]