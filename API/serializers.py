from rest_framework import serializers
from apps.posts.models import Post
from apps.users.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name')


class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'created_at')
