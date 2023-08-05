from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.http import Http404

class ProfileDeleteViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client = Client()
        self.login_url = reverse('login_user')
        self.profile_delete_url = reverse('delete_profile', kwargs={'pk': self.user.pk})
        self.client.login(username='testuser', password='testpassword')

    def test_profile_delete_view_exists(self):
        response = self.client.get(self.profile_delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_auth_app/user_confirm_delete.html')

    def test_profile_delete_view_post(self):
        response = self.client.post(self.profile_delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index_page'))
        self.assertFalse(get_user_model().objects.filter(id=self.user.id).exists())
