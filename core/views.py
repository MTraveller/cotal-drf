from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        queryset = Profile.objects.select_related('link').all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('OK')


@api_view()
def profile_detail(request, id):
    profile = get_object_or_404(Profile, pk=id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)
