from django.conf.urls import url

from stu import views
urlpatterns = [
    url(r'allstudent/(\d+)/', views.AllStu, name='alls'),
    url(r'redirectStu/(?P<g_id>\d+)/', views.redirectStu, name='reStu'),
    # /s/selstu/2018/4/1/
    url(r'selstu/(\d+)/(\d+)/(\d+)/', views.selStu),
    url(r'actstu/(?P<year>\d+)/(?P<month>\d+)/(?P<days>\d+)/', views.actStu),
    url(r'delstu', views.DelStu),
    url(r'upstu', views.upStu)

]

