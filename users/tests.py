from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User

class UserLoginTest(APITestCase):
    def setUp(self):
        self.data = {'username':'test', 'password':'testpassword', 'fullname':'required :(', 'email':'test@test.com'}
    
    def test_signup(self):
        url = reverse('user_view')
        response = self.client.post(url, self.data)
        self.assertEqual(response.data['message'], '가입 완료!!')
