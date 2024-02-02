from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('apps.users.urls', 'apps.users'), namespace='users')),
    path('posts/', include(('apps.posts.urls', 'apps.posts'), namespace='posts')),
    path('api/', include(('API.urls', 'API'), namespace='api')),
]
