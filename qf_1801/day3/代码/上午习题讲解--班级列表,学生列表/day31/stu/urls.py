from django.conf.urls import url

from stu import views
urlpatterns = [
    url(r'allstu/', views.allstu)
]