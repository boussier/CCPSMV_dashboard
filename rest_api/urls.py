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
    path('agroofapi/', TemplateView.as_view(template_name="about.html")),
    path('agroofapi/admin/', admin.site.urls),
    path('agroofapi/v1/auth/', include('apiauth.urls')),
    path('agroofapi/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('agroofapi/schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('agroofapi/schema/redoc/',SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] 
