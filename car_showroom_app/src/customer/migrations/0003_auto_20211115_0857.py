# Generated by Django 3.2.8 on 2021-11-15 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]