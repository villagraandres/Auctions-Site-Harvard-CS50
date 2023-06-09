# Generated by Django 4.1.6 on 2023-03-26 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_alter_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='closed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 16, 9, 24, 316694, tzinfo=datetime.timezone.utc)),
        ),
    ]
