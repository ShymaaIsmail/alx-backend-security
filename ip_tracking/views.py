from django.http import JsonResponse
from django_ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='10/m', method='POST', block=True)
@ratelimit(key='ip', rate='5/m', method='GET', block=True)
def login(request):
    return JsonResponse({"message": "Login successful"})
