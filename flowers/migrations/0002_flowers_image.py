# Generated by Django 2.2 on 2020-12-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='flowers/'),
        ),
    ]
