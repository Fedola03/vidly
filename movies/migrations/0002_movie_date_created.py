# Generated by Django 4.2.2 on 2023-06-08 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 8, 13, 34, 48, 395464, tzinfo=datetime.timezone.utc)),
        ),
    ]
