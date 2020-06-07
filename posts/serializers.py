from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth import get_user_model

User = get_user_model()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()
