# Generated by Django 3.2 on 2021-05-11 07:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210511_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='notation',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]