from django.urls import path
from django.views.generic import TemplateView
from apps.posts.views import CreatePost, ListPosts, DetailPost, comment

urlpatterns = [
    path('', TemplateView.as_view(template_name='posts/home.html'), name='home'),
    path('new/', CreatePost.as_view(), name='create'),
    path('list/', ListPosts.as_view(), name='list-posts'),
    path('detail/<int:pk>', DetailPost.as_view(), name='detail-post'),
    path('list-category/', TemplateView.as_view(template_name='posts/home.html'), name='list-category'),
    path('comment/', comment, name='create-comment'),
]
