from django.db import models
from django.core import validators, exceptions


def validate_string_starts_with_a_letter(value):
    if not value[0].isalpha():
        raise exceptions.ValidationError("Your name must start with a letter!")


def validate_string_contains_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError("Fruit name should contain only letters!")


# Create your models here.

class ProfileModel(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MIN_LEN_LAST_NAME = 1
    MIN_LEN_PASSWORD = 8

    first_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
                    validate_string_starts_with_a_letter))

    last_name = models.CharField(
        max_length=35,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_LEN_LAST_NAME),
                    validate_string_starts_with_a_letter))

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False)

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_LEN_PASSWORD),))

    image_url = models.URLField(
        null=True,
        blank=True)

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True)


class FruitModel(models.Model):
    MIN_LEN_FRUIT_NAME = 2

    name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        validators=(validators.MinLengthValidator(MIN_LEN_FRUIT_NAME),
                    validate_string_contains_only_letters))

    image_url = models.URLField(
        null=False,
        blank=False)

    description = models.TextField(
        null=False,
        blank=False)

    nutrition = models.TextField(
        null=True,
        blank=True)