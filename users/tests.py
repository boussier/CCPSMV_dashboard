from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from .models import CustomUser
from .serializers import UserDetailsSerializer
from rest_framework.test import APIClient

REGISTRATION_URL = reverse('rest_register')
LOGIN_URL = reverse('rest_login')
PASSWORD_CHANGE_URL = reverse('rest_password_change')
USER_DETAIL_URL = reverse('rest_user_details')
LOGOUT_URL = reverse('rest_logout')

class UsersApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()       
        response = self.client.post(REGISTRATION_URL, {
                         'email': 'test@test.com',
                         'password1': 'hakunamatata',
                         'password2': 'hakunamatata',
                         'first_name' : 'john',
                         'last_name': 'doe'
                         }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)      
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['token'])
    
    def test_password_change(self):        
        response = self.client.post(PASSWORD_CHANGE_URL, {
                         'new_password1': 'hdgstgehst01',
                         'new_password2': 'hdgstgehst01',
                         }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        
    def test_get_user_details(self):        
        response = self.client.get(USER_DETAIL_URL)
        user_details = CustomUser.objects.get(email='test@test.com')
        serializer = UserDetailsSerializer(user_details)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_logout(self):        
        response = self.client.post(LOGOUT_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)    
        self.client.logout()
        response = self.client.get(USER_DETAIL_URL)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
