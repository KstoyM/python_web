from datetime import date
from django.test import TestCase
from final_exam_project.user_auth_app.models import User
from final_exam_project.rent_a_car_web.forms import RentCarForm
from final_exam_project.rent_a_car_web.models import Car


class RentCarFormTest(TestCase):

    def test_rent_car_form_save(self):
        user = User.objects.create_user(username='testuser', password='testpassword', age=20)
        car = Car.objects.create(make='Test', car_model='Test', price=50, horsepower=200)
        form = RentCarForm(data={'date_from': date(2023, 8, 1), 'date_to': date(2023, 8, 5)}, car=car)

        self.assertTrue(form.is_valid())
        rent_car = form.save(commit=False)

        rent_car.user = user

        rent_car.save()

        self.assertEqual(rent_car.car, car)
        self.assertEqual(rent_car.user, user)
        self.assertEqual(rent_car.date_from, date(2023, 8, 1))
        self.assertEqual(rent_car.date_to, date(2023, 8, 5))
        self.assertIsNotNone(rent_car.created_at)
        self.assertIsNotNone(rent_car.modified_at)

    def test_rent_car_form_save_without_commit(self):
        user = User.objects.create_user(username='testuser', password='testpassword', age=20)
        car = Car.objects.create(make='Test', car_model='Test', price=50, horsepower=200)
        form = RentCarForm(data={'date_from': date(2023, 8, 1), 'date_to': date(2023, 8, 5)}, car=car)

        self.assertTrue(form.is_valid())
        rent_car = form.save(commit=False)

        rent_car.user = user
        rent_car.save()

        self.assertEqual(rent_car.car, car)
        self.assertEqual(rent_car.user, user)
        self.assertEqual(rent_car.date_from, date(2023, 8, 1))
        self.assertEqual(rent_car.date_to, date(2023, 8, 5))
        self.assertIsNotNone(rent_car.created_at)
        self.assertIsNotNone(rent_car.modified_at)
