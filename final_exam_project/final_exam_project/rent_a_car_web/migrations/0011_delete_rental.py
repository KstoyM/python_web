# Generated by Django 4.2.2 on 2023-08-05 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_car_web', '0010_remove_car_currently_rented_car_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rental',
        ),
    ]