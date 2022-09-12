# Generated by Django 4.1 on 2022-08-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='variables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.FloatField(verbose_name='Latitud (dd)')),
                ('longitud', models.FloatField(verbose_name='Longitud (dd)')),
                ('velocidad', models.FloatField(verbose_name='Velocidad (m/s)')),
                ('altitud', models.FloatField(verbose_name='Altitud (m)')),
                ('error_altitud', models.FloatField(blank=True, null=True, verbose_name='Error altitud (m)')),
                ('rest_bateria', models.FloatField(verbose_name='Bateria restante (%)')),
                ('temp_bateria', models.FloatField(verbose_name='Temperatura bateria (°)')),
                ('volt_bateria', models.FloatField(verbose_name='Voltaje bateria (V)')),
                ('curr_bateria', models.FloatField(verbose_name='Corriente bateria (A)')),
            ],
        ),
    ]
