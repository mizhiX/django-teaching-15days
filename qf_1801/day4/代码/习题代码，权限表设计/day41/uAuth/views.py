from django.http import HttpResponse
from django.shortcuts import render

from uAuth.models import Users, Role, Permission


def TestPermission(request):

    user = Users.objects.get(id=1)
    u_p = user.role.p.all()
    print(u_p)
    return HttpResponse('查询成功')
