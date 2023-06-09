# Generated by Django 4.1.6 on 2023-03-23 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_list_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Products',
            field=models.ManyToManyField(related_name='products', to='auctions.list'),
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 16, 53, 47, 94831, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
