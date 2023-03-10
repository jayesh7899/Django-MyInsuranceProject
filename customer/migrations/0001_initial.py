# Generated by Django 3.1.12 on 2022-05-17 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
