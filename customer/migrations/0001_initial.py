# Generated by Django 3.2.12 on 2022-02-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=25)),
                ('last_name', models.TextField(max_length=25)),
                ('contact_no', models.TextField(max_length=15)),
                ('pincode', models.IntegerField(default=0)),
            ],
        ),
    ]
