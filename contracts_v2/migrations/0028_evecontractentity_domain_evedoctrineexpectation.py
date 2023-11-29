# Generated by Django 4.1.5 on 2023-06-28 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0012_evedoctrine_primary'),
        ('contracts_v2', '0027_alter_evecontractentity_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='evecontractentity',
            name='domain',
            field=models.CharField(choices=[('Public Seeding', 'Public Seeding'), ('Public Doctrine Seeding', 'Public Doctrine Seeding'), ('Alliance Doctrine Seeding', 'Alliance Doctrine Seeding')], default='Public Seeding', max_length=32),
        ),
        migrations.CreateModel(
            name='EveDoctrineExpectation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('public', 'Public'), ('alliance', 'Alliance')], max_length=32)),
                ('doctrine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleets.evedoctrine')),
                ('entities', models.ManyToManyField(blank=True, related_name='doctrine_expectations', to='contracts_v2.evecontractentity')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctrine_expectations', to='contracts_v2.evecontractlocation')),
            ],
        ),
    ]
