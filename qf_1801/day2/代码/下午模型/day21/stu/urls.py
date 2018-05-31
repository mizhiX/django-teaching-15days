# -*- coding:utf-8 -*-

from django.conf.urls import url

from stu import views

urlpatterns = [
    # 创建学生信息
    url(r'addstu', views.addStu),
    url(r'selstu/', views.selectStu)
]