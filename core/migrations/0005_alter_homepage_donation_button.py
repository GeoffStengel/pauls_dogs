# Generated by Django 5.1.1 on 2024-10-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_homepage_donation_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='donation_button',
            field=models.URLField(default='https://square.link/u/y3l6efc0'),
        ),
    ]
