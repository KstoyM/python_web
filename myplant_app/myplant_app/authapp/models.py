from django.db import models


# Create your models here.

class ProfileModel(models.Model):
    username = models.CharField(max_length=30)  # TODO: validators
    first_name = models.CharField()