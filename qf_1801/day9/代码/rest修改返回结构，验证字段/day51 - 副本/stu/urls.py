from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'^student', views.StudentEdit)

urlpatterns = [
    url(r'^aStuPage/', views.aStuPage),
    url(r'^index/', views.index),
    url(r'^stuPage/', views.stuPage),
    url(r'^addstu/', views.addStu, name='add'),
    url(r'^addstuInfo/(?P<stu_id>\d+)/', views.addStuInfo, name='addinfo'),
    url(r'^showStu/', views.showStus)

]

urlpatterns += router.urls
