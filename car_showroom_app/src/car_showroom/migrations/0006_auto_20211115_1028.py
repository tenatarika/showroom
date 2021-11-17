# Generated by Django 3.2.8 on 2021-11-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_showroom', '0005_showroomsale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsofshowroom',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='showroomsale',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]
