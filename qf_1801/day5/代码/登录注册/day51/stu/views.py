from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from stu.models import Student, StudentInfo

def index(request):

    if request.method == 'GET':
        # 获取所有学生信息
        stuinfos = StudentInfo.objects.all()
        return render(request, 'index.html', {'stuinfos':stuinfos})

def addStu(request):

    if request.method == 'GET':

        return  render(request, 'addStu.html')

    if request.method == 'POST':
        # 跳转到学习详情方法中去
        name = request.POST.get('name')
        tel = request.POST.get('tel')

        stu = Student.objects.create(s_name=name, s_tel=tel)

        return HttpResponseRedirect(
            reverse('s:addinfo', kwargs={'stu_id': stu.id})
        )


def addStuInfo(request, stu_id):

    if request.method == 'GET':

        return render(request, 'addStuInfo.html', {'stu_id':stu_id})

    if request.method == 'POST':

        stu_id = request.POST.get('stu_id')
        addr = request.POST.get('addr')

        StudentInfo.objects.create(i_addr=addr, s_id=stu_id)

        return HttpResponseRedirect('/stu/index/')
