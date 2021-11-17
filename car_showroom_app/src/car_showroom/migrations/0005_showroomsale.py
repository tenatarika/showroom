# Generated by Django 3.2.8 on 2021-11-15 09:30

from django.db import migrations, models
import django.db.models.deletion
import src.tools.fields


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_auto_20211115_0857'),
        ('car_showroom', '0004_auto_20211115_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowroomSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('discount', src.tools.fields.DecimalRangeField(decimal_places=2, default=1, max_digits=10)),
                ('end_date', models.DateField(auto_now_add=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cars_showroom_sale', related_query_name='car_showroom_sale', to='supplier.car', to_field='vin')),
                ('showroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sales_showroom', related_query_name='sale_showroom', to='car_showroom.carshowroom')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
