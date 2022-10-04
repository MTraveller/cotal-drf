from django.http import HttpResponse, HttpResponseRedirect


def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('/api/v1/')


def api_root(request):
    if request.method == 'GET':
        return HttpResponse('Welcome to Cotal API.')
