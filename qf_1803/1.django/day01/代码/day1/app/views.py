from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 登录验证
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 验证用户名和密码是否能从数据库中匹配到user对象
        # User.objects.filter(username=username, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            # 验证通过
            auth.login(request, user)
            # return render(request, 'index.html')
            return HttpResponseRedirect(reverse('a:index'))
        else:
            # 验证不通过
            return render(request, 'login.html')


def register(request):
    # 注册
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        # 第一种
        # return HttpResponseRedirect('/app/login/')
        # 第二种
        return HttpResponseRedirect(reverse('a:login'))


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('a:login'))


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def head(request):
    if request.method == 'GET':
        return render(request, 'head.html')


def left(request):
    if request.method == 'GET':
        return render(request, 'left.html')


def grade(request):
    if request.method == 'GET':
        return render(request, 'grade.html')


def addstu(request):
    if request.method == 'GET':
        return render(request, 'addstu.html')


def student(request):
    if request.method == 'GET':
        return render(request, 'student.html')


def addgrade(request):
    if request.method == 'GET':
        return render(request, 'addgrade.html')

