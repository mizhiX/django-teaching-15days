
from django.utils.deprecation import MiddlewareMixin

from stu.models import Visit

import logging

logger = logging.getLogger('auth')

class VisitTimes(MiddlewareMixin):

    def process_request(self, request):

        # 统计访问的url以及次数
        path = request.path
        try:
            visit = Visit.objects.get(v_url=path)
            if visit:
                visit.v_times += 1
                visit.save()
        except Exception as e:
            print(e)
            logger.error(e)
            Visit.objects.create(v_url=path, v_times=1)

