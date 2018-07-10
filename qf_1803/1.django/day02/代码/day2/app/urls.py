
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app import views

urlpatterns = [
    # django自带登录注册注销
    url('^login/$', views.login, name='login'),
    url('^register/$', views.register),
    url('^logout/$', views.logout),
    # 手动实现登录注册注销
    url('my_register/', views.my_register, name='my_register'),
    url('my_login/', views.my_login, name='my_login'),

    url('index/', views.index, name='index'),
    url('head/', views.head, name='head'),
    url('left/', views.left, name='left'),
    url('^grade/$', views.grade, name='grade'),
    url('addstu/', views.addstu, name='addstu'),
    url('student/', views.student, name='student'),
    url('addgrade/', views.addgrade, name='addgrade'),
    url('delstu/', views.delstu, name='delstu'),
    url('editgrade/', views.editgrade, name='editgrade'),



]

