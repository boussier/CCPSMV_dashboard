"""
rest_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [    
    path(f'{settings.API_BASE_URL}/', TemplateView.as_view(template_name="about.html")),
    path(f'{settings.API_BASE_URL}/admin/', admin.site.urls),
    path(f'{settings.API_BASE_URL}/v1/auth/', include('apiauth.urls')),
    path(f'{settings.API_BASE_URL}/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(f'{settings.API_BASE_URL}/schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path(f'{settings.API_BASE_URL}/schema/redoc/',SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] 
