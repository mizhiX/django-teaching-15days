
from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^left/', views.left, name='left'),
    url(r'^grade/', views.grade, name='grade'),
    url(r'^head/', views.head, name='head'),
    url(r'^addgrade/', views.addgrade, name='addgrade'),
    url(r'^student/', views.students, name='student'),
    url(r'^addstu/', views.addstu, name='addstu'),
    url(r'^delstu/', views.delstu, name='delstu'),
    url(r'^editgrade/', views.editgrade, name='editgrade'),

]