# Generated by Django 5.0.6 on 2024-06-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_usertickets'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='duration',
            field=models.IntegerField(default=1, help_text='Duration in days'),
        ),
    ]
