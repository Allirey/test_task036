from django.core import exceptions
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.views import APIView, Response
from .serializers import PostSerializer
from .models import Post, Like


class PostViewSet(viewsets.ModelViewSet):
    model = Post
    queryset = Post.objects
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class LikeView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)

        if not post.likes.filter(author=user).first():
            Like.objects.create(post=post, author=user)

            return Response({'message': 'Liked'}, 201)
        else:
            return Response({'message': 'Like already exist'}, 400)


class UnlikeView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, post_id):
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        try:
            like = post.likes.get(author=user)
            like.delete()
            return Response({'message': 'Unliked'}, 201)
        except Like.DoesNotExist:
            return Response({"message": 'Like doesn\'t exist'}, 400)


class LikeAnalytics(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        try:
            records = Like.objects.filter(created__range=[date_from, date_to]).extra(select={'day': "date(created)"}) \
                .values('day').order_by('day').annotate(likes_number=Count('id'))

        except exceptions.ValidationError as e:
            records = []

        return Response(records)
