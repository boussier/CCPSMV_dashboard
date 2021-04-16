"""
rest_api URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  url
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.views.generic import TemplateView

urlpatterns = [    
    path('restapi/', TemplateView.as_view(template_name="about.html")),
    path('restapi/admin/', admin.site.urls),
    path('restapi/v1/auth/', include('apiauth.urls')),
    path('restapi/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('restapi/schema/swagger-ui/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('restapi/schema/redoc/',SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] 
