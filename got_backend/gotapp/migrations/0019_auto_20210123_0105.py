# Generated by Django 3.1.5 on 2021-01-23 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gotapp', '0018_odcinekweryfikowany_trasa'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='uczestnictwo',
            unique_together={('turysta', 'wycieczka')},
        ),
        migrations.AlterUniqueTogether(
            name='uprawnienie',
            unique_together={('legitymacja', 'grupaGorska')},
        ),
    ]
