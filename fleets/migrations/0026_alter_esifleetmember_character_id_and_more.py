# Generated by Django 4.0.10 on 2023-07-11 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0025_evefleetmotdtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esifleetmember',
            name='character_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmember',
            name='ship_type_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmember',
            name='solar_system_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmember',
            name='squad_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmember',
            name='station_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='esifleetmember',
            name='wing_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmembertrackinglog',
            name='ship_type_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmembertrackinglog',
            name='solar_system_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='esifleetmembertrackinglog',
            name='station_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
