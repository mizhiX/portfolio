# Generated by Django 2.0.7 on 2018-07-13 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180713_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='images/error_1.png', upload_to='images/'),
        ),
    ]
