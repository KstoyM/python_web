from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
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


def validate_min_age(value):
    if value < 18 or value > 100:
        raise exceptions.ValidationError('You must be between 18 and 100 years old to register.')


class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(auth_models.AbstractUser, auth_models.PermissionsMixin):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 30

    objects = AppUserManager()

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True,
        validators=(MinLengthValidator(USERNAME_MIN_LEN), validate_string_alphanumeric)

    )

    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=FIRST_NAME_MAX_LEN,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LEN),
                    validate_string_only_letters)

    )

    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=LAST_NAME_MAX_LEN,
        validators=(MinLengthValidator(LAST_NAME_MIN_LEN)
                    , validate_string_only_letters)
    )

    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=False, blank=False, validators=(validate_min_age,))
    profile_picture = models.URLField(blank=True, null=True)
    user_permissions = models.ManyToManyField(auth_models.Permission, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
