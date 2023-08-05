from django.test import TestCase, Client
from django.urls import reverse
from final_exam_project.rent_a_car_web.models import Car


class IndexPageViewTest(TestCase):

    def setUp(self):
        self.car1 = Car.objects.create(make='Toyota', car_model='Corolla', horsepower=200, image='toyota.jpg', price=50)
        self.car2 = Car.objects.create(make='Honda', car_model='Civic', horsepower=180, image='honda.jpg', price=45)

    def test_index_page_returns_correct_template(self):
        client = Client()
        response = client.get(reverse('index_page'))

        self.assertTemplateUsed(response, 'index.html')

    def test_index_page_displays_cars(self):
        client = Client()
        response = client.get(reverse('index_page'))

        self.assertIn('cars', response.context)
        cars_in_context = response.context['cars']

        self.assertQuerysetEqual(cars_in_context, Car.objects.all(), ordered=False)
