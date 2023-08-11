from django.test import TestCase
from final_exam_project.rent_a_car_web.forms import CarForm


class CarFormTest(TestCase):

    def test_car_form_valid_data(self):
        form = CarForm(data={
            'make': 'Test',
            'car_model': 'Test',
            'price': 50,
            'horsepower': 200,
            'image': 'https://example.com/test.jpg',
        })
        self.assertTrue(form.is_valid())

    def test_car_form_missing_required_field(self):
        form = CarForm(data={
            'car_model': 'Test',
            'price': 50,
            'horsepower': 200,
            'image': 'https://example.com/test.jpg',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('make', form.errors)

    def test_car_form_invalid_price(self):
        form = CarForm(data={
            'make': 'Test',
            'car_model': 'Test',
            'price': -50,
            'horsepower': 200,
            'image': 'https://example.com/test.jpg',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors)

    def test_car_form_empty_fields(self):
        form = CarForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('make', form.errors)
        self.assertIn('car_model', form.errors)
        self.assertIn('price', form.errors)
        self.assertIn('horsepower', form.errors)
        self.assertIn('image', form.errors)
