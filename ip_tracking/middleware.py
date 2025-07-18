import ipinfo
from django.core.cache import cache
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from ipware import get_client_ip

from .models import RequestLog, BlockedIP

import os

IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
ipinfo_handler = ipinfo.getHandler(IPINFO_TOKEN)


class LogIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, _ = get_client_ip(request)
        if not ip:
            return

        # Check blacklist
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Forbidden: Your IP is blocked.")

        # Geolocation caching
        geo_data = cache.get(f"geo:{ip}")
        if not geo_data:
            try:
                details = ipinfo_handler.getDetails(ip)
                geo_data = {
                    "country": details.country_name or "",
                    "city": details.city or "",
                }
                cache.set(f"geo:{ip}", geo_data, timeout=86400)
            except Exception:
                geo_data = {"country": "", "city": ""}

        # Save log
        RequestLog.objects.create(
            ip_address=ip,
            path=request.path,
            country=geo_data["country"],
            city=geo_data["city"]
        )
