from django.urls import path
from .api_views import check_ip

urlpatterns = [
    path('check-ip/', check_ip, name='check-ip'),
]
