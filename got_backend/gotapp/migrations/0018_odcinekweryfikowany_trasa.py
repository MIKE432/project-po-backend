# Generated by Django 3.1.5 on 2021-01-22 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gotapp', '0017_auto_20210122_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='odcinekweryfikowany',
            name='trasa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='odcinki', to='gotapp.trasa'),
        ),
    ]
