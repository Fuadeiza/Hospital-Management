# Generated by Django 3.0.6 on 2020-05-31 09:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MgtApp', '0005_auto_20200530_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='date_of_consultation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
