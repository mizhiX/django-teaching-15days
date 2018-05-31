
from datetime import datetime

from django.utils.deprecation import MiddlewareMixin

from axf.models import UserTicketModel

class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):

        ticket = request.COOKIES.get('ticket')

        if not ticket:
            return None

        user_ticket = UserTicketModel.objects.filter(ticket=ticket)
        if user_ticket:
            # 判断令牌是否有效，无效则删除
            out_time = user_ticket[0].out_time.replace(tzinfo=None)
            now_time = datetime.utcnow()

            if out_time > now_time:
                # 没有失效
                request.user = user_ticket[0].user
            else:
                user_ticket.delete()
