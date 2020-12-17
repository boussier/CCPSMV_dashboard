from rest_framework import serializers
from users.models import CustomUser
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer, UserDetailsSerializer as RestAuthUserDetailsSerializer
from rest_auth.registration.serializers import RegisterSerializer as RestAuthRegisterSerializer
from allauth.account import app_settings as allauth_settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser   
        fields = '__all__'    
        fields = ('first_name', 'last_name', 'email')

class UserDetailsSerializer(RestAuthUserDetailsSerializer):    
    class Meta:
        model = CustomUser
        fields = ('pk', 'email', 'first_name', 'last_name', 'weight', 'age', 'height', 'photo')
        read_only_fields = ('email', )

class LoginSerializer(RestAuthLoginSerializer):   
    username = None

class RegisterSerializer(RestAuthRegisterSerializer):
    username = None
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)   
  

