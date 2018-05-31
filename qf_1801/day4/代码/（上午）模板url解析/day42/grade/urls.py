
from django.conf.urls import url

from grade import views

urlpatterns = [
    url(r'allgrade/', views.AllGrade)
]