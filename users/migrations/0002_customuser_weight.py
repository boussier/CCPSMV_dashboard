# Generated by Django 3.1.4 on 2020-12-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
