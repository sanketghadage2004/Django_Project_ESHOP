# Generated by Django 4.0.1 on 2022-03-02 11:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_remove_payment_transaction_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 2, 16, 51, 32, 411918)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 2, 16, 51, 32, 412918)),
        ),
    ]
