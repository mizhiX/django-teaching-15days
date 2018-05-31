from django.conf.urls import url

from stu import views
urlpatterns = [
    url(r'allstudent/(\d+)/', views.AllStu, name='alls')
]