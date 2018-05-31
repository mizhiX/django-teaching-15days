from django.conf.urls import url

from grade import views
urlpatterns = [
    url(r'^grades/', views.showGrades)
]