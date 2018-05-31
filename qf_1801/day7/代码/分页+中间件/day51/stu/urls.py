from django.conf.urls import url

from stu import views
urlpatterns = [
    url(r'^aStuPage/', views.aStuPage),
    url(r'^index/', views.index),
    url(r'^stuPage/', views.stuPage),
    url(r'^addstu/', views.addStu, name='add'),
    url(r'^addstuInfo/(?P<stu_id>\d+)/', views.addStuInfo, name='addinfo')
]