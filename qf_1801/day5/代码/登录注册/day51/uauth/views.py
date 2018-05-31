from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from uauth.models import Users


def regist(request):

    if request.method == 'GET':

        return render(request, 'register.html')

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

        return render(request, 'login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Users.objects.filter(u_name=name).exists():
            user = Users.objects.get(u_name=name)
            if check_password(password, user.u_password):
                ticket = 'agdoajbfjad'
                # 绑定令牌到cookie里面
                response = HttpResponse()
                response.set_cookie('ticket', ticket)
                # 存在服务段
                user.u_ticket = ticket
                user.save()
                return response
            else:
                return HttpResponse('用户密码错误')
        else:
            return HttpResponse('用户不存在')