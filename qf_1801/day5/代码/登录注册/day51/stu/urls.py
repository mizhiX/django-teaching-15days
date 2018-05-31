from django.conf.urls import url

from stu import views
urlpatterns = [
    url(r'^index/', views.index),
    url(r'^addstu/', views.addStu, name='add'),
    url(r'^addstuInfo/(?P<stu_id>\d+)/', views.addStuInfo, name='addinfo')
]