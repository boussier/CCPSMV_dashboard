from rest_framework import generics
from rest_auth import views as rest_auth_views
from rest_auth.registration import views as rest_auth_registration_views
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from users.serializers import RegisterSerializer, UserDetailsSerializer


class LoginView(rest_auth_views.LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.\\ 
    Accept the following POST parameters: email, password\\
    Return the REST Framework Token Object's key.
    """


class LogoutView(rest_auth_views.LogoutView):
    """
    Calls logout method and delete the Token object
    assigned to the current User object.\\
    Accepts/Returns nothing.
    """


class UserDetailsView(rest_auth_views.UserDetailsView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods. \\    
    Read-only fields: pk, email
    Returns UserModel fields.
    """
    serializer_class = UserDetailsSerializer



class PasswordResetView(rest_auth_views.PasswordResetView):
    """
    Accepts the following POST parameters: email\\
    Returns the success/fail message.
    """


class PasswordResetConfirmView(rest_auth_views.PasswordResetConfirmView):
    """
    Password reset e-mail link is confirmed, therefore this resets the user's password.\\
    Accepts the following POST parameters: token, uid, new_password1, new_password2\\
    Returns the success/fail message.
    """


class PasswordChangeView(rest_auth_views.PasswordChangeView):
    """
    Accepts the following POST parameters: new_password1, new_password2\\
    Returns the success/fail message.
    """


class RegisterView(rest_auth_registration_views.RegisterView):
    """
    TEST
    """
    serializer_class = RegisterSerializer



class VerifyEmailView(rest_auth_registration_views.VerifyEmailView):
    """
    TEST
    """
