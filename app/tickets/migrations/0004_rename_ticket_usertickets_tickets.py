# Generated by Django 5.0.6 on 2024-06-12 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_tickets_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertickets',
            old_name='ticket',
            new_name='tickets',
        ),
    ]