from django.http import HttpResponse, HttpResponseRedirect


def handle_404_redirect(request, *args, **kwargs):
    return HttpResponseRedirect('/api/v1/')


def api_root(request):
    if request.method == 'GET':
        return HttpResponse('Welcome to Cotal API.')
