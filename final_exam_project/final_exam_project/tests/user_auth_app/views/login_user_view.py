from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

class LoginUserViewTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login_user')
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

    def test_login_view_uses_correct_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'login_page.html')

    def test_login_successful(self):
        response = self.client.post(self.login_url, self.login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('index_page'))

        # Check if the user is logged in
        self.assertIn('_auth_user_id', self.client.session)

    def test_login_unsuccessful(self):
        wrong_login_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, wrong_login_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login_page.html')

        self.assertNotIn('_auth_user_id', self.client.session)

    def test_login_form_instance(self):
        response = self.client.get(self.login_url)
        form = response.context['form']
        self.assertIsInstance(form, AuthenticationForm)
