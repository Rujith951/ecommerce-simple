# Generated by Django 5.0 on 2023-12-21 10:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_cart_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="dateCreated",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
