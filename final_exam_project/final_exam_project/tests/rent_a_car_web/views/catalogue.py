from django.test import TestCase
from django.urls import reverse
from final_exam_project.rent_a_car_web.models import Car

class CarsPageViewTest(TestCase):
    def test_cars_page_view(self):
        self.car1 = Car.objects.create(make='Toyota', car_model='Corolla', horsepower=200, image='toyota.jpg', price=50)
        self.car2 = Car.objects.create(make='Honda', car_model='Civic', horsepower=180, image='honda.jpg', price=45)

        response = self.client.get(reverse('catalogue_page'))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'catalogue_page.html')

        self.assertIn('cars', response.context)

        cars_in_context = response.context['cars']

        self.assertQuerysetEqual(cars_in_context, Car.objects.all(), ordered=False)