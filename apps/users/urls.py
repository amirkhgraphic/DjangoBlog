from apps.users.views import SignupView, LoginView
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('signup/', SignupView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='log-in'),
    path('logout/', auth_views.LogoutView.as_view(), name='log-out'),
]
