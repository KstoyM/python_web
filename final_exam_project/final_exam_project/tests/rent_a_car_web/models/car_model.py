from django.contrib.auth import get_user_model
from django.test import TestCase

from final_exam_project.rent_a_car_web.models import RentCar, Car
from final_exam_project.user_auth_app.models import User

User = get_user_model()


class RentCarModelTest(TestCase):
    def setUp(self):
        self.car = Car.objects.create(
            make='Toyota',
            car_model='Camry',
            horsepower=200,
            image='https://example.com/camry.jpg',
            price=100.00,
        )

        self.user = User.objects.create(
            username='testuser',
            password='testpassword',
            age=20,
        )

    def test_rent_car_model_creation(self):
        rent_car = RentCar.objects.create(
            car=self.car,
            date_from='2023-08-01',
            date_to='2023-08-05',
            price=250.00,
            user=self.user,
        )
        self.assertIsInstance(rent_car, RentCar)
        self.assertEqual(rent_car.car, self.car)
        self.assertEqual(rent_car.date_from, '2023-08-01')
        self.assertEqual(rent_car.date_to, '2023-08-05')
        self.assertEqual(rent_car.price, 250.00)
        self.assertEqual(rent_car.user, self.user)

    def test_rent_car_model_fields_validation(self):
        with self.assertRaises(Exception):
            RentCar.objects.create(
                date_from='2023-08-01',
                date_to='2023-08-05',
                price=250.00,
                user=self.user,
            )

        with self.assertRaises(Exception):
            RentCar.objects.create(
                car=self.car,
                date_from='2023-08-01',
                date_to='2023-08-05',
                price=250.00,
            )
