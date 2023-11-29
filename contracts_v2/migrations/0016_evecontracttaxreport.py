# Generated by Django 4.1.5 on 2023-03-25 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts_v2', '0015_evecontractexpectation_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveContractTaxReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('start_range', models.DateField(default=datetime.datetime(2023, 2, 23, 23, 22, 4, 696072))),
                ('end_range', models.DateField(default=datetime.datetime(2023, 3, 25, 23, 22, 4, 696181))),
                ('report', models.TextField()),
            ],
        ),
    ]
