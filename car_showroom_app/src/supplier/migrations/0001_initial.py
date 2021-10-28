# Generated by Django 3.2.8 on 2021-10-25 08:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('width', models.IntegerField(blank=True)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.PositiveIntegerField(blank=True, default='1900')),
                ('color', models.CharField(blank=True, default='white', max_length=200)),
                ('vin', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(regex='^[A-HJ-NPR-Za-hj-npr-z\\d]{8}')])),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=255)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.car', to_field='vin')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='supplier',
            name='cars',
            field=models.ManyToManyField(through='supplier.SupplierCar', to='supplier.Car'),
        ),
    ]