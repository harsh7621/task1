# Generated by Django 3.2.12 on 2022-02-08 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20220208_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='product_id',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 16, 17, 41, 295944)),
        ),
    ]
