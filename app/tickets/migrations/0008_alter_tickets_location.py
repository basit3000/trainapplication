# Generated by Django 5.0.6 on 2024-06-26 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_locations_city_locations_state_locations_zip_code'),
        ('tickets', '0007_alter_tickets_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='locations.locations'),
        ),
    ]
