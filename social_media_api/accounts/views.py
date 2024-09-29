from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import User  # Ensure User is your custom user model
from .serializers import UserSerializer

# Use generics.GenericAPIView for both follow and unfollow

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()  # Assuming User is your CustomUser model

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(User, id=user_id)
        if request.user == user_to_follow:
            return Response({'detail': "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({'detail': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(User, id=user_id)
        if request.user == user_to_unfollow:
            return Response({'detail': "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.remove(user_to_unfollow)
        return Response({'detail': f'You have unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
