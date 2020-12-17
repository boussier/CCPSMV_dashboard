from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms as d_forms
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class PhyaSignupForm(SignupForm):

    # Put in custom signup logic
    def custom_signup(self, request, user):
        # Set the user's type from the form reponse
        user.weight = self.cleaned_data["weight"]
        # Save the user's type to their database record
        user.save()
