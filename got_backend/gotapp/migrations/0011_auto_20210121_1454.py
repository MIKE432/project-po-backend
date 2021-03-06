# Generated by Django 3.1.5 on 2021-01-21 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gotapp', '0010_auto_20210121_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uprawnienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataWaznosci', models.DateField()),
                ('dataPrzyznania', models.DateField()),
                ('grupaGorska', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotapp.grupagorska')),
                ('legitymacja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gotapp.legitymacja')),
            ],
        ),
        migrations.AddField(
            model_name='legitymacja',
            name='uprawnienia',
            field=models.ManyToManyField(through='gotapp.Uprawnienie', to='gotapp.GrupaGorska'),
        ),
    ]
