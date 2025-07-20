from django.urls import path
from .api_views import check_ip
from . import views
urlpatterns = [
    path('check-ip/', check_ip, name='check-ip'),
    path('login/', views.login, name='login'),
]
