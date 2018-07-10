from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from app.models import MyUser


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        path = ['/app/my_login/', '/app/my_register/']
        if request.path in path:
            return None

        ticket = request.COOKIES.get('ticket')
        if ticket:
            user = MyUser.objects.filter(ticket=ticket)
            if user:
                return None
            else:
                return HttpResponseRedirect(reverse('a:my_login'))
        else:
            return HttpResponseRedirect(reverse('a:my_login'))