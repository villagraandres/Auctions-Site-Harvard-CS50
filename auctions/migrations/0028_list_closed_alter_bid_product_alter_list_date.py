# Generated by Django 4.1.6 on 2023-03-26 22:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_list_date_bid'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='closed',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidsProduct', to='auctions.list'),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 16, 6, 56, 95912, tzinfo=datetime.timezone.utc)),
        ),
    ]
