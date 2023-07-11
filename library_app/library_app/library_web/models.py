from django.db import models


# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    image_url = models.URLField(blank=False, null=False)


class Book(models.Model):
    title = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.URLField(blank=False, null=False)
    book_type = models.CharField(max_length=30, blank=False, null=False)
