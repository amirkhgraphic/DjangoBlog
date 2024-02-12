from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='posts/home.html'), name='home'),
    path('users/', include(('apps.users.urls', 'apps.users'), namespace='users')),
    path('posts/', include(('apps.posts.urls', 'apps.posts'), namespace='posts')),
    path('api/', include(('API.urls', 'API'), namespace='api')),
]
