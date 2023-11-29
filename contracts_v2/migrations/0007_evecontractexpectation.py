# Generated by Django 4.1.5 on 2023-03-12 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts_v2', '0006_esientitycontractresponse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EveContractExpectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_name', models.CharField(max_length=255)),
                ('ship_type_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('type', models.IntegerField(choices=[(1, '[NVY-1]'), (2, '[NVY-5]'), (3, '[NVY-30]')])),
                ('size', models.IntegerField(choices=[(1, 'Scout'), (2, 'Small'), (3, 'Medium'), (4, 'Large'), (5, 'Open')])),
            ],
        ),
    ]
