# Generated by Django 4.2.2 on 2023-07-27 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]
