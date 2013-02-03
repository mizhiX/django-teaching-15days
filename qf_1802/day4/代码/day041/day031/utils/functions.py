from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse

from user.models import Users


def is_login(func):
    def check_login(request):
        # 如果登录，返回函数func
        ticket = request.COOKIES.get('ticket')
        if not ticket:
            # 没有登录，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        user = Users.objects.filter(ticket=ticket)
        if not user:
            # 没有登录，跳转到登录页面
            return HttpResponseRedirect(reverse('user:login'))
        return func(request)
    return check_login