# Generated by Django 4.1.6 on 2023-03-26 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_list_closed_alter_bid_product_alter_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 16, 7, 32, 520919, tzinfo=datetime.timezone.utc)),
        ),
    ]
