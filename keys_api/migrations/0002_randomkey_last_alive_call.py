# Generated by Django 2.2.11 on 2020-07-17 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keys_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomkey',
            name='last_alive_call',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
