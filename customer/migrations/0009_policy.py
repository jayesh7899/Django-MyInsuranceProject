# Generated by Django 3.1.12 on 2022-05-26 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20220524_0842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('sumassu', models.CharField(max_length=60)),
                ('primium', models.CharField(max_length=60)),
                ('tenure', models.CharField(max_length=60)),
            ],
        ),
    ]
