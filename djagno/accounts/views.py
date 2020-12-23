from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)