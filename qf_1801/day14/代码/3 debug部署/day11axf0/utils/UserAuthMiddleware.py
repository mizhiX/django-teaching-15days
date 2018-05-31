from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse

from axf.models import UserTicketModel

from day11axf import settings

from datetime import datetime, timedelta


class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        ticket = request.COOKIES.get('ticket')

        if not ticket:
            pass

        userticket = UserTicketModel.objects.filter(ticket=ticket)
        if userticket:
            if userticket[0].out_time.replace(tzinfo=None) > datetime.utcnow():
                request.user = userticket[0].user
            else:
                out_time = datetime.now() + timedelta(days=1)
                UserTicketModel.objects.filter(ticket=ticket,
                                               out_time=out_time).delete()

