# Generated by Django 4.1.6 on 2023-03-24 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_remove_user_products_list_user_id_alter_list_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 12, 30, 0, 367088, tzinfo=datetime.timezone.utc)),
        ),
    ]
