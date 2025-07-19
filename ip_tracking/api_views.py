from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def check_ip(request):
    ip = request.META.get('REMOTE_ADDR', '')
    return Response({
        "message": "Your IP address",
        "ip": ip
    })
