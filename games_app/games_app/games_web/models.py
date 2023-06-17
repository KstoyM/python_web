from django.core import validators, exceptions
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.

class Profile(models.Model):
    MIN_AGE = 12

    email = models.EmailField(null=False, blank=False)
    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),),
        null=False,
        blank=False, )
    password = models.CharField(max_length=30, null=False, blank=False)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)


class GameModel(models.Model):
    CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other')
    )

    title = models.CharField(max_length=30, null=False, blank=False, unique=True)
    category = models.CharField(max_length=15, null=False, blank=False, choices=CHOICES)
    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ))
    max_level = models.IntegerField(null=True, blank=True, validators=(
        validators.MinValueValidator(1),), verbose_name='Max Level')
    image_url = models.URLField(null=False, blank=False, verbose_name='Image URL')
    summary = models.TextField(null=True, blank=True)
