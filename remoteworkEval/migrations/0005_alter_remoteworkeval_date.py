# Generated by Django 3.2 on 2021-05-15 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('remoteworkEval', '0004_auto_20210515_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remoteworkeval',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 15, 10, 14, 32, 137320, tzinfo=utc)),
        ),
    ]