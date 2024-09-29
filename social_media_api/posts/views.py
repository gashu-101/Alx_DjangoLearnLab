from rest_framework import status, generics
from rest_framework import permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
   
        post = generics.get_object_or_404(Post,pk=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=request.user, post=post)
        
        # Create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )
        
        return Response({"detail": "Post liked."}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            return Response({"detail": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
