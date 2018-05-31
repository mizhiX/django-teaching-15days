
# -*-  coding:utf-8 -*-
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'hello/', views.first_hello),
    url(r'girl/', views.girl_hello)
]
