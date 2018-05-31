from django.shortcuts import render

from rest_framework import mixins, viewsets

from stu.models import Student, StudentInfo
from stu.serializers import StuSerializers


def index(request):

    return render(request, 'index.html')


class AllStudent(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):

    # 去查询所有的数据
    queryset = Student.objects.all()
    # 序列化(表现层,将数据按照一定格式返回给用户)
    serializer_class = StuSerializers
