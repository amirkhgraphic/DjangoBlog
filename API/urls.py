from django.urls import path
from API.views import GetPostsListAPIView, GetPostSearchAPIView, GetPostCategoryAPIView, GetPostAuthorAPIView

urlpatterns = [
    path('list-posts/', GetPostsListAPIView.as_view(), name='list-posts'),
    path('search-title/', GetPostSearchAPIView.as_view(), name='search-title'),
    path('search-category/', GetPostCategoryAPIView.as_view(), name='search-category'),
    path('search-author/', GetPostAuthorAPIView.as_view(), name='search-author'),
]
