# Generated by Django 4.1.5 on 2023-04-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0006_evedoctrinetag'),
    ]

    operations = [
        migrations.AddField(
            model_name='evedoctrine',
            name='tags',
            field=models.ManyToManyField(blank=True, to='fleets.evedoctrinetag'),
        ),
    ]
