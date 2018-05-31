from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse

from grade.models import Student


def AllStu(request, g_id):
    # stus = Student.objects.filter(g_id=g_id)
    #
    # return render(request, 'students.html', {'stus': stus})
    # 业务逻辑

    return HttpResponseRedirect(
        reverse('s:reStu', kwargs={'g_id':g_id})
    )

def redirectStu(request, g_id):

    stus = Student.objects.filter(g_id=g_id)

    return render(request, 'students.html', {'stus': stus})

def selStu(request, n, m, p):

    return HttpResponse('获取url传递多个参数的方法')

def actStu(request, month, days, year):

    return HttpResponse('获取url中指定的参数')

def DelStu(request):
    stu_id = request.GET.get('stu_id')
    Student.objects.filter(id=stu_id).delete()

    return HttpResponseRedirect('/g/allgrade/')

def upStu(request):
    stu_id = request.GET.get('stu_id')
    # stu = Student.objects.get(id=stu_id)
    # stu.s_name = '修改的名字'
    # stu.save()
    Student.objects.filter(id=stu_id).update(s_name='大乔')
    return HttpResponseRedirect('/g/allgrade/')

