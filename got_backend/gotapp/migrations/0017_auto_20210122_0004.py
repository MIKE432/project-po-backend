# Generated by Django 3.1.5 on 2021-01-21 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gotapp', '0016_auto_20210121_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trasa',
            name='wycieczki',
        ),
        migrations.RemoveField(
            model_name='wycieczka',
            name='trasy',
        ),
        migrations.AddField(
            model_name='wycieczka',
            name='trasa',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wycieczka', to='gotapp.trasa'),
        ),
    ]
