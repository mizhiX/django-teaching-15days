
import random
import time

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from uauth.models import Users


def regist(request):

    if request.method == 'GET':

        return render(request, 'day6_regist.html')

    if request.method == 'POST':
        # 注册
        name = request.POST.get('name')
        password = request.POST.get('password')
        password = make_password(password)

        Users.objects.create(u_name=name,
                             u_password=password)
        return HttpResponseRedirect('/uauth/login/')

def login(request):

    if request.method == 'GET':

        return render(request, 'day6_login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Users.objects.filter(u_name=name).exists():
            user = Users.objects.get(u_name=name)
            if check_password(password, user.u_password):
                s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
                ticket = ''
                for i in range(15):
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK_' + ticket + str(now_time)
                # ticket = 'agdoajbfjad'
                # 绑定令牌到cookie里面
                # response = HttpResponse('登录成功')
                response = HttpResponseRedirect('/stu/index/')
                # max_age 存活时间
                response.set_cookie('ticket', ticket, max_age=3000)
                # 存在服务段
                user.u_ticket = ticket
                user.save()
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, 'day6_login.html', {'password': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, 'day6_login.html', {'name':'用户不存在'})

def logout(request):

    if request.method == 'GET':
        response = HttpResponseRedirect('/uauth/login/')
        response.delete_cookie('ticket')
        return response