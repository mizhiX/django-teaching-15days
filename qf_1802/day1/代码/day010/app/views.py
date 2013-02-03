from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect

from django.core.urlresolvers import reverse

from app.models import Grade, Student

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
        paginator = Paginator(grades, 3)
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
        stus = Student.objects.all()
        return render(request, 'student.html', {'stus':stus})

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
        #  获取班级信息
        grade = Grade.objects.filter(id=g_id).first()
        # 创建学生信息
        # Student.objects.create(s_name=s_name, g_id=grade.id)/
        Student.objects.create(s_name=s_name, g=grade)

        # stu = Student(s_name=s_name, g=grade)
        # stu.save()
        return HttpResponseRedirect(reverse('app:student'))



