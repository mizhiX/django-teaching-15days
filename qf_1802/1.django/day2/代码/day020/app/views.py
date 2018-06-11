from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect

from django.core.urlresolvers import reverse

from app.models import Grade, Student
from day010.settings import PAGE_NUMBERS
from user.models import Users

'''
首页
'''
def index(request):

    if request.method == 'GET':
        return render(request, 'index.html')

'''
左侧菜单栏
'''
def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')

'''
班级列表
'''
def grade(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        grades = Grade.objects.all()
        paginator = Paginator(grades, PAGE_NUMBERS)
        pages = paginator.page(int(page_num))
        return render(request, 'grade.html', {'grades':grades, 'pages':pages})

'''
添加班级页面
'''
def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')

    if request.method == 'POST':
        # 创建班级信息
        g_name = request.POST.get('grade_name')
        g = Grade()
        g.g_name = g_name
        g.save()
        return HttpResponseRedirect(reverse('app:grade'))



'''
头部页面
'''
def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')

'''
学生列表
'''
def students(request):
    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        stus = Student.objects.all()
        paginator = Paginator(stus, PAGE_NUMBERS)
        pages = paginator.page(int(page_num))
        return render(request, 'student.html', {'stus':stus, 'pages':pages})

'''
添加学生信息
'''
def addstu(request):
    if request.method == 'GET':
        grades = Grade.objects.all()
        return render(request, 'addstu.html', {'grades':grades})

    if request.method == 'POST':

        s_name = request.POST.get('s_name')
        g_id = request.POST.get('g_id')

        s_img = request.FILES.get('s_img')
        #  获取班级信息
        grade = Grade.objects.filter(id=g_id).first()
        # 创建学生信息
        # Student.objects.create(s_name=s_name, g_id=grade.id)/
        Student.objects.create(s_name=s_name,
                               g=grade,
                               s_img=s_img)

        # stu = Student(s_name=s_name, g=grade)
        # stu.save()
        return HttpResponseRedirect(reverse('app:student'))


'''
删除学生
'''
def delstu(request):
    if request.method == 'GET':
        s_id = request.GET.get('s_id')
        Student.objects.filter(id=s_id).delete()

        return HttpResponseRedirect(reverse('app:student'))

'''
编辑班级信息
'''
def editgrade(request):

    if request.method == 'GET':
        grade_id = request.GET.get('grade_id')
        return render(request, 'addgrade.html', {'grade_id':grade_id})

    if request.method == 'POST':

        grade_id = request.POST.get('grade_id')
        grade_name = request.POST.get('grade_name')

        g = Grade.objects.filter(pk=grade_id).first()
        g.g_name = grade_name
        g.save()

        return HttpResponseRedirect(reverse('app:grade'))

