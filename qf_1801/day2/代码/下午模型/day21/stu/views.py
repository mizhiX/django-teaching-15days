
# -*- coding:utf-8 -*-
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render

from stu.models import Student


def addStu(request):
    # 添加学生信息
    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        # 处理提交的学生信息

        stu_name = request.POST.get('name')
        if request.POST.get('sex') == '男':
            stu_sex = 1
        else:
            stu_sex = 0
        stu_birth = request.POST.get('birth')
        stu_tel = request.POST.get('tel')

        # stu = Student()
        # stu.stu_name = stu_name
        # stu.stu_birth = stu_birth
        # stu.stu_sex = stu_sex
        # stu.stu_tel = stu_tel
        # stu.save()

        Student.objects.create(
            stu_name = stu_name,
            stu_birth = stu_birth,
            stu_sex = stu_sex,
            stu_tel = stu_tel
        )

        return HttpResponse('添加学生信息成功')

def selectStu(request):
    # 查询数据
    # stus = Student.objects.all()
    # 查询所有女生
    # stus = Student.objects.filter(stu_sex=False)
    #get()
    # stus = Student.objects.get(id=10)
    # stus = Student.objects.get(stu_sex=True)
    # 查询id从大到小的排序
    # stus = Student.objects.all().order_by('-id')
    # 获取id最大的一条数据
    # stus = Student.objects.all().order_by('-id').first()
    # 获取id最小的一条数据
    # stus = Student.objects.all().order_by('-id').last()
    # 获取男的的数据的个数
    # stus = Student.objects.filter(stu_sex=True).count()
    # print(stus)
    # 查询所有80后女生的信息
    # stus = Student.objects.filter(stu_sex=False).\
    #     filter(stu_birth__gte='1980-01-01').\
    #     filter(stu_birth__lt='1990-01-01')
    # stus = Student.objects.filter(stu_sex=False,
    #                               stu_birth__gte='1980-01-01',
    #                               stu_birth__lt='1990-01-01')
    # return render(request, 'detail.html', {'stus': stus})

    # 查询姓李的数据
    # stus = Student.objects.filter(stu_name__startswith='李')
    # 查询姓名以华结束的数据
    # stus = Student.objects.filter(stu_name__endswith='华')

    # 姓名中包含李的数据
    # stus = Student.objects.filter(stu_name__contains='李')

    # 判断是否存在张三
    # stus = Student.objects.filter(stu_name='小乔').exists()
    # print(stus)

    # 获取指定多个id的值
    # ids = [1,2]
    # stus = Student.objects.filter(id__in=ids)

    # 查询语文成绩大于等于数学成绩的学生
    # stus = Student.objects.filter(stu_yuwen__gte=F('stu_shuxue'))

    # 查询语文成绩超过数学成绩10分的学生
    # stus = Student.objects.filter(stu_yuwen__gte=F('stu_shuxue') + 10)

    # 查询学生姓名不叫李白的，或者语文成绩大于80分的学生

    # ~ 代表非
    # stus = Student.objects.filter(~Q(stu_name='李白') | Q(stu_yuwen__gt=80))
    stus = Student.objects.filter(~Q(stu_name='李白') & Q(stu_yuwen__gt=80))

    # 返回给前端
    return render(request, 'sel_stu.html', {'stus': stus})
