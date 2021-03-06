# Generated by Django 3.0.6 on 2020-05-30 18:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis', models.CharField(max_length=256)),
                ('age', models.PositiveIntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('date_of_consultation', models.DateTimeField(default=datetime.datetime(2020, 5, 30, 18, 25, 37, 477147, tzinfo=utc))),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
