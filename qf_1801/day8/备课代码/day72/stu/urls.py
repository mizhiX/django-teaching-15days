from django.conf.urls import url


from stu import views
# urlpatterns = [
#     url(r'^addStu/', views.AllStudent.as_view),
# ]

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'^addStu', views.AllStudent)

urlpatterns = [
    url(r'^index/', views.index)
]
urlpatterns += router.urls
