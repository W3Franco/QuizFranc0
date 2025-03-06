from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import UserSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view

@api_view(['POST'])
def token_obtain_pair(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })
