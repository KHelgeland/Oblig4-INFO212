# Generated by Django 4.1.2 on 2022-10-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0002_alter_car_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car", name="year", field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name="customer", name="age", field=models.CharField(max_length=3),
        ),
    ]