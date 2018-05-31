from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student
# Create your views here.

def addStudent(request):

    stu = Student()
    stu.name = '张三'
    stu.sex = 1

    stu.save()

    return HttpResponse('添加成功')
