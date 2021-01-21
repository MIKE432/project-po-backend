# Generated by Django 3.1.5 on 2021-01-20 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['region'],
            },
        ),
        migrations.CreateModel(
            name='GrupaGorska',
            fields=[
                ('kodGrupy', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nazwa', models.CharField(max_length=255)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotapp.region')),
            ],
            options={
                'ordering': ['kodGrupy', 'nazwa'],
            },
        ),
    ]
