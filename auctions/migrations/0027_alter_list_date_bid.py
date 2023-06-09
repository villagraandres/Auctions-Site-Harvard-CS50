# Generated by Django 4.1.6 on 2023-03-24 20:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_alter_list_date_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 14, 23, 24, 750266, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.list')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
