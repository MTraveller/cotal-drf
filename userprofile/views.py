from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


@api_view()
def profile_list(request):
    queryset = Profile.objects.select_related('link').all()
    serializer = ProfileSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def profile_detail(request, id):
    profile = get_object_or_404(Profile, pk=id)
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)
