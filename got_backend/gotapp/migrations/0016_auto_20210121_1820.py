# Generated by Django 3.1.5 on 2021-01-21 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gotapp', '0015_auto_20210121_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odcinekweryfikowany',
            name='odcinek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='odcinki', to='gotapp.odcinek'),
        ),
        migrations.CreateModel(
            name='Trasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=40)),
                ('sumaPunkt', models.IntegerField()),
                ('dataPocz', models.DateField()),
                ('dataKonc', models.DateField()),
                ('wycieczki', models.ManyToManyField(to='gotapp.Wycieczka')),
            ],
        ),
        migrations.AddField(
            model_name='wycieczka',
            name='trasy',
            field=models.ManyToManyField(to='gotapp.Trasa'),
        ),
    ]
