# Generated by Django 3.1.5 on 2021-01-23 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gotapp', '0021_auto_20210123_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odcinek',
            name='dlugosc',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='odcinek',
            name='przewyzszenie',
            field=models.FloatField(default=0),
        ),
    ]
