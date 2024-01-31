from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/landing_page.html'), name='home'),
    path('list/', TemplateView.as_view(template_name='home/landing_page.html'), name='list-posts'),
]
