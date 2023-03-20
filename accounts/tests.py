from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Account

class LoginAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login_with_correct_credentials(self):
        response = self.client.post('/api/login/', {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK, "test_login_with_correct_credentials passed")

    def test_login_with_incorrect_credentials(self):
        response = self.client.post('/api/login/', {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "test_login_with_incorrect_credentials passed")

    def test_login_with_missing_username(self):
        response = self.client.post('/api/login/', {
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "test_login_with_missing_username passed")

    def test_login_with_missing_password(self):
        response = self.client.post('/api/login/', {
            'username': 'testuser',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "test_login_with_missing_password passed")

    def test_login_with_non_existent_user(self):
        response = self.client.post('/api/login/', {
            'username': 'nonexistentuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "test_login_with_non_existent_user passed")

    def test_login_with_invalid_username_format(self):
        response = self.client.post('/api/login/', {
            'username': 'testuser@',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "test_login_with_invalid_username_format passed")

    def test_login_with_invalid_password_format(self):
        response = self.client.post('/api/login/', {
            'username': 'testuser',
            'password': '',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, "test_login_with_invalid_password_format passed")