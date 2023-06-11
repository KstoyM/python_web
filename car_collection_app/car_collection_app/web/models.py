from enum import Enum

from django.core import validators
from django.db import models

from car_collection_app.web.validators import valid_year_validator


# Create your models here.


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MIN_AGE = 18

    username = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME, 'The username must be a minimum of 2 chars'),
        ))

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_AGE),
        ))

    password = models.CharField(
        max_length=30,
        blank=False,
        null=False, )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True, )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True, )

    profile_picture = models.URLField(
        blank=True,
        null=True, )


class Car(models.Model):
    MIN_CHAR_MODEL = 2
    MIN_PRICE_VALUE = 1

    TYPES = (
        ("Sport Car", "Sport Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    car_type = models.CharField(
        max_length=10,
        choices=TYPES,
        blank=False,
        null=False,
        verbose_name='Type')

    model = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_CHAR_MODEL),)
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            valid_year_validator,)
    )

    image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Image URL')

    price = models.FloatField(
        blank=False,
        null=False,
        validators=(
            validators.MinValueValidator(MIN_PRICE_VALUE),)
    )
