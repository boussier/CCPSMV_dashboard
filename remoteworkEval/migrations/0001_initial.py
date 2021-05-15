# Generated by Django 3.2 on 2021-05-15 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteWorkEval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('mail', models.IntegerField(blank=True, null=True, verbose_name='Courrier')),
                ('archiving', models.IntegerField(blank=True, null=True, verbose_name='Archivage')),
                ('instruction', models.IntegerField(blank=True, null=True, verbose_name='Instruction')),
                ('filesFollowUp', models.IntegerField(blank=True, null=True, verbose_name='Suivi dossiers')),
                ('meetingPreparation', models.IntegerField(blank=True, null=True, verbose_name='Préparation réunion ou compte rendu')),
                ('others', models.IntegerField(blank=True, null=True, verbose_name='Autres')),
            ],
            options={
                'verbose_name': 'Evaluation période de télétravail',
            },
        ),
    ]
