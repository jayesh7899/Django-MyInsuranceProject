# Generated by Django 3.1.12 on 2022-05-24 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_categary'),
    ]

    operations = [
        migrations.AddField(
            model_name='categary',
            name='dt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
