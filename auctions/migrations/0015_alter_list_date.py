# Generated by Django 4.1.6 on 2023-03-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_alter_list_date_alter_list_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
