from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


def api_root(request):
    if request.method == 'GET':
        return HttpResponse('Welcome to Cotal API.')


@api_view(['GET'])
def api_start_endpoint(request):
    if request.method == 'GET':
        return Response({
            'detail': 'Welcome to Cotal API. '
            'From here you can query all known endpoints.'
        })
