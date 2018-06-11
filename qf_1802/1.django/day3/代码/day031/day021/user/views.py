
import random

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth

from django.core.urlresolvers import reverse

from user.models import Users


'''
注册
'''
def djregister(request):

    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if not all([username, pwd1, pwd2]):
            msg = '请填写完所有参数'
            return render(request, 'register.html', {'msg': msg})

        if pwd1 != pwd2:
            msg = '两次密码不一致'
            return render(request, 'register.html', {'msg': msg})

        User.objects.create_user(username=username, password=pwd1)

        return HttpResponseRedirect(reverse('app:djlogin'))

'''
登录
'''
def djlogin(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 返回验证成功的用户信息
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('app:index'))
        else:
            msg = '用户名或者密码错误'
            return render(request, 'login.html', {'msg': msg})

'''
注销
'''
def djlogout(request):

    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:djlogin'))


'''
自己实现登录注册
'''
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':

        username = request.POST.get('username')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if not all([username, pwd1, pwd2]):
            msg = '注册信息不能为空'
            return render(request, 'register.html', {'msg': msg})
        if pwd1 != pwd2:
            msg = '两次密码必须一致'
            return render(request, 'register.html', {'msg': msg})

        Users.objects.create(username=username, password=pwd1)

        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = Users.objects.filter(username=username,
                                    password=password).first()
        if user:
            # 先产生随机的字符串， 长度28
            s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            ticket = ''
            for i in range(28):
                ticket += random.choice(s)
            # 保存在服务端
            user.ticket = ticket
            user.save()
            # 保存在客户端，cookies
            response = HttpResponseRedirect(reverse('app:index'))
            response.set_cookie('ticket', ticket)

            return response

def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('user:login'))
        response.delete_cookie('ticket')
        return response


def userper(request):
    # 查询妲己有那些权限
    # 1. 先查询妲己这个用户
    # 2. 在查询角色
    # 3. 通过角色id去查询权限
    user = Users.objects.filter(username='妲己').first()
    u_r_p = user.role.r_p.all()
    # 判断妲己是否有学生列表的权限
    u_r_p.filter(p_en='STUDENTLIS').exists()
    pass