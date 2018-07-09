
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from app import views

urlpatterns = [
    url('login/', views.login, name='login'),
    url('register/', views.register),
    url('logout/', views.logout),
    url('index/', login_required(views.index), name='index'),
    url('head/', views.head, name='head'),
    url('left/', views.left, name='left'),
    url('^grade/$', login_required(views.grade), name='grade'),
    url('addstu/', login_required(views.addstu), name='addstu'),
    url('student/', login_required(views.student), name='student'),
    url('^addgrade/', login_required(views.addgrade), name='addgrade'),
]

