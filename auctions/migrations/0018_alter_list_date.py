# Generated by Django 4.1.6 on 2023-03-23 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_alter_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 16, 35, 31, 611187, tzinfo=datetime.timezone.utc)),
        ),
    ]
