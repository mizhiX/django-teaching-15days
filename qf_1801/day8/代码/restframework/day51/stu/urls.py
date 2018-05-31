from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'^student', views.StudentEdit)

urlpatterns = [
    url(r'^aStuPage/', login_required(views.aStuPage)),
    url(r'^index/', login_required(views.index)),
    url(r'^stuPage/', login_required(views.stuPage)),
    url(r'^addstu/', login_required(views.addStu), name='add'),
    url(r'^addstuInfo/(?P<stu_id>\d+)/', login_required(views.addStuInfo), name='addinfo')
]

urlpatterns += router.urls
