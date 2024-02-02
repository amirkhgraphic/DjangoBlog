from django.urls import path
from django.views.generic import TemplateView
from apps.posts.views import CreatePost, ListPosts, DetailPost, comment, CategoryListPosts, AuthorListPosts

urlpatterns = [
    path('', TemplateView.as_view(template_name='posts/home.html'), name='home'),
    path('new/', CreatePost.as_view(), name='create'),
    path('list/', ListPosts.as_view(), name='list-posts'),
    path('detail/<int:pk>', DetailPost.as_view(), name='detail-post'),
    path('comment/', comment, name='create-comment'),
    path('list-category/', CategoryListPosts.as_view(), name='list-category'),
    path('list-author/', AuthorListPosts.as_view(), name='list-author'),
]
