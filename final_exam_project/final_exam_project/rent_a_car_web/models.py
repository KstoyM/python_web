from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    horsepower = models.IntegerField(default=0)
    image = models.URLField(blank=False, null=False)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def is_car_rented(self, date_from, date_to):
        return RentCar.objects.filter(car=self, date_from__lte=date_to, date_to__gte=date_from).exists()


class RentCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('user_auth_app.User', on_delete=models.CASCADE)
