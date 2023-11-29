# Generated by Django 4.1.5 on 2023-06-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculators', '0002_freightroute_midpoints'),
    ]

    operations = [
        migrations.AddField(
            model_name='freightroute',
            name='isk_jump',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightroute',
            name='isk_m3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='freightroute',
            name='jump_freight_capable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='freightroute',
            name='jumps',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
