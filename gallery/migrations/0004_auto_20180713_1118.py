# Generated by Django 2.0.7 on 2018-07-13 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20180713_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='img',
            field=models.ImageField(default='error_1.png', upload_to='images/'),
        ),
    ]
