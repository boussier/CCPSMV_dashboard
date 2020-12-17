from django.urls import include, path
from django.views.generic import TemplateView
from .views import (
    LoginView, LogoutView, UserDetailsView, 
    PasswordChangeView, PasswordResetView, PasswordResetConfirmView,
    RegisterView, VerifyEmailView
)
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token
from django.contrib.auth.views import PasswordResetConfirmView

urlpatterns = [
    path('api-token-verify/', verify_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('password/reset/', PasswordResetView.as_view(),name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(),name='rest_password_reset_confirm'),
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('password/change/', PasswordChangeView.as_view(),name='rest_password_change'),
    path('registration', RegisterView.as_view(), name='rest_register'),
    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/<key>/', TemplateView.as_view(),name='account_confirm_email'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
]
