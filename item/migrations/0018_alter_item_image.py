# Generated by Django 5.1.1 on 2024-11-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0017_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='ppp/'),
        ),
    ]