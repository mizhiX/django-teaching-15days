
from django.conf.urls import url

from user import views

urlpatterns = [
    # django自带登录注册
    url(r'^djregister/', views.djregister, name='djregister'),
    url(r'^djlogin/', views.djlogin, name='djlogin'),
    url(r'^djlogout/', views.djlogout, name='djlogout'),

    # 自己实现
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),

    # 权限/角色
    url(r'^userper/', views.userper, name='userper'),
]