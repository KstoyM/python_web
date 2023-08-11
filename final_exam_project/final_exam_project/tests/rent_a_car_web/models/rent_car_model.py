from django.test import TestCase
from django.utils import timezone
from final_exam_project.rent_a_car_web.models import RentCar, Car
from final_exam_project.user_auth_app.models import User


class RentCarModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpassword', age=20)
        cls.car = Car.objects.create(make='Lambo', car_model='Any', price=150)

    def test_rentcar_creation(self):
        rentcar = RentCar.objects.create(
            car=self.car,
            date_from=timezone.now().date(),
            date_to=timezone.now().date() + timezone.timedelta(days=7),
            price=150,
            user=self.user
        )
        self.assertTrue(isinstance(rentcar, RentCar))
        self.assertEqual(rentcar.car.make, 'Lambo')
        self.assertEqual(rentcar.car.car_model, 'Any')
        self.assertEqual(rentcar.car.price, 150)
        self.assertEqual(rentcar.date_from, timezone.now().date())
        self.assertEqual(rentcar.date_to, timezone.now().date() + timezone.timedelta(days=7))

