from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from final_exam_project.rent_a_car_web.models import Car


class AddCarsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.User = get_user_model()

        cls.user = cls.User.objects.create_user(username='testuser', password='testpassword', age=20)
        cls.superuser_group = Group.objects.create(name='Superuser')
        cls.staff_group = Group.objects.create(name='Is_Staff')
        cls.user.groups.add(cls.superuser_group)

    def setUp(self):
        self.car_data = {
            'make': 'Trabant',
            'car_model': '500',
            'horsepower': 999,
            'image': 'https://silodrome.com/wp-content/uploads/2022/03/Trabant-Car-1600x1067.jpg',
            'price': 50,
        }

    def test_add_cars_view_requires_authentication(self):
        client = Client()
        response = client.get(reverse('add_cars'))
        self.assertEqual(response.status_code, 302)

    def test_add_cars_view_accessible_by_authorized_user(self):
        client = Client()
        client.force_login(self.user)
        response = client.get(reverse('add_cars'))
        self.assertEqual(response.status_code, 200)

    def test_add_cars_view_can_add_car(self):
        client = Client()
        client.force_login(self.user)
        response = client.post(reverse('add_cars'), data=self.car_data)
        car = Car.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Car.objects.count(), 1)
        self.assertEqual(car.make, 'Trabant')
        self.assertEqual(car.car_model, '500')
        self.assertEqual(car.horsepower, 999)
        self.assertEqual(car.image, 'https://silodrome.com/wp-content/uploads/2022/03/Trabant-Car-1600x1067.jpg')
        self.assertEqual(car.price, 50)

    def test_add_cars_view_redirects_to_index_page_on_success(self):
        client = Client()
        client.force_login(self.user)
        response = client.post(reverse('add_cars'), data=self.car_data)
        self.assertRedirects(response, reverse('index_page'))
