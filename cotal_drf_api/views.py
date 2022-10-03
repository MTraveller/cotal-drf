from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response


def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('/api/v1/')


def api_root(request):
    if request.method == 'GET':
        return HttpResponse('Welcome to Cotal API.')
