# Generated by Django 4.1.6 on 2023-03-24 18:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_alter_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Products',
        ),
        migrations.AddField(
            model_name='list',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userId', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 24, 12, 25, 3, 63493, tzinfo=datetime.timezone.utc)),
        ),
    ]