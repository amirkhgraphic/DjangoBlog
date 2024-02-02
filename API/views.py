from django.db.models import Q
from API.serializers import PostListSerializer
from rest_framework.generics import ListAPIView
from apps.posts.models import Post


class GetPostsListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostListSerializer


class GetPostSearchAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostListSerializer

    def get_queryset(self):
        key = self.request.query_params.get('Key', None)
        return self.queryset.filter(Q(title__icontains=key) | Q(body__icontains=key))


class GetPostCategoryAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostListSerializer

    def get_queryset(self):
        key = self.request.query_params.get('Key', None)
        return self.queryset.filter(category__name__icontains=key)


class GetPostAuthorAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostListSerializer

    def get_queryset(self):
        key = self.request.query_params.get('Key', None)
        return self.queryset.filter(author__user_name__icontains=key)
