# Generated by Django 3.1.7 on 2021-03-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_cities_city_can_go3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('savedTime', models.TimeField(blank=True, null=True)),
            ],
        ),
    ]
