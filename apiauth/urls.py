from django.urls import include, path
from django.views.generic import TemplateView
from .views import (
    LoginView, LogoutView, UserDetailsView,
    PasswordChangeView, PasswordResetView, PasswordResetConfirmView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('accounts/', include('rest_registration.api.urls')),
    path('user/', UserDetailsView.as_view(), name='rest_user_details')
]
