from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user == user_to_follow:
        return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    if request.user == user_to_unfollow:
        return Response({'detail': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
