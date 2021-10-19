# Generated by Django 3.2.8 on 2021-10-19 18:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import src.car_showroom.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=14)),
                ('sortquery', models.JSONField(blank=True, default=src.car_showroom.models.jsonfield_default_value)),
                ('country', django_countries.fields.CountryField(blank=True, default=None, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CarsOfShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.car', to_field='vin')),
                ('сarShowroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_showroom.carshowroom')),
            ],
        ),
        migrations.AddField(
            model_name='carshowroom',
            name='cars',
            field=models.ManyToManyField(through='car_showroom.CarsOfShowroom', to='supplier.Car'),
        ),
    ]
