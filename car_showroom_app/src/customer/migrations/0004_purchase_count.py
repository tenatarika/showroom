# Generated by Django 3.2.8 on 2021-11-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20211115_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]