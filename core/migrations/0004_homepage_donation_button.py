# Generated by Django 5.1.1 on 2024-10-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_homepage_sponsor_01_img_homepage_sponsor_02_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='donation_button',
            field=models.URLField(default='https://example.com/donate'),
        ),
    ]