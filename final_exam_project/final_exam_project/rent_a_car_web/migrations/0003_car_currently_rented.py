# Generated by Django 4.2.2 on 2023-07-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_car_web', '0002_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='currently_rented',
            field=models.BooleanField(default=False),
        ),
    ]