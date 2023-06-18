from django.core import validators
from django.db import models


def validate_name_capitalized(value):
    if not value[0].isupper():
        raise validators.ValidationError("Your name must start with a capital letter!")


# Create your models here.

class ProfileModel(models.Model):
    MIN_LEN_USERNAME = 2
    username = models.CharField(max_length=10, blank=False, null=False,
                                validators=(validators.MinLengthValidator(MIN_LEN_USERNAME),))
    first_name = models.CharField(max_length=20, blank=False, null=False, validators=(validate_name_capitalized,))
    last_name = models.CharField(max_length=20, blank=False, null=False, validators=(validate_name_capitalized,))
    profile_picture = models.URLField(blank=True, null=True)


class PlantModel(models.Model):
    CHOICES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )
    MIN_LEN_NAME = 2

    plant_type = models.CharField(max_length=14, blank=False, null=False, choices=CHOICES)
    name = models.CharField(max_length=20, blank=False, null=False,
                            validators=(validators.MinLengthValidator(MIN_LEN_NAME),))
    image_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
