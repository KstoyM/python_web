# Generated by Django 4.2.2 on 2023-06-24 06:33

import django.core.validators
from django.db import migrations, models
import fruitipedia_app.fruitipedia_web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), fruitipedia_app.fruitipedia_web.models.validate_string_contains_only_letters])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), fruitipedia_app.fruitipedia_web.models.validate_string_starts_with_a_letter])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), fruitipedia_app.fruitipedia_web.models.validate_string_starts_with_a_letter])),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
