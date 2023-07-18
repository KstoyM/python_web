from django.core import exceptions
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models


def validate_string_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError('Ensure this value contains only letters, numbers, and underscore.')


def validate_string_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Ensure this value contains only letters.')


class User(auth_models.AbstractUser):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
        validators=(MinLengthValidator(USERNAME_MIN_LEN), validate_string_alphanumeric)

    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LEN),
                    validate_string_only_letters)
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MIN_LEN)
                    , validate_string_only_letters)
    )

    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
