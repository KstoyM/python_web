from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


def validate_not_a_negative_number(value):
    if value < 0:
        raise ValidationError("Price cannot be negative")


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    horsepower = models.IntegerField(default=0, validators=[validate_not_a_negative_number])
    image = models.URLField(blank=False, null=False)
    price = models.FloatField(default=0, validators=[validate_not_a_negative_number])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def is_car_rented(self, date_from, date_to):
        return RentCar.objects.filter(car=self, date_from__lte=date_to, date_to__gte=date_from).exists()


class RentCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    price = models.FloatField(default=0, validators=[validate_not_a_negative_number])
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('user_auth_app.User', on_delete=models.CASCADE)

    def clean(self):
        if self.date_to and self.date_from:
            if self.date_to < self.date_from:
                raise ValidationError("The end date cannot be before the start date.")

    def save(self, *args, **kwargs):  # fixing the annoying timezone error
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        super(RentCar, self).save(*args, **kwargs)
