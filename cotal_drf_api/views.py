import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect


def handle_redirect(request, *args, **kwargs):

    return HttpResponseRedirect(settings.API_ENDPOINT)


def api_root(request):
    if request.method == 'GET':
        return HttpResponse('Welcome to Cotal API.')
