from ..ip_trackingee.models import RequestLog
from django.utils.deprecation import MiddlewareMixin
from ipware import get_client_ip

class LogIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, _ = get_client_ip(request)
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path
        )
