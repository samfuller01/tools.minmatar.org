# Generated by Django 4.1.5 on 2023-10-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0030_alter_evefleetdiscordwebhook_webhook_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='evefleetdiscordwebhook',
            name='channel_id',
            field=models.CharField(default=1127086469631180830, max_length=255),
            preserve_default=False,
        ),
    ]
