# Generated by Django 4.1 on 2022-08-29 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TelemetryApp', '0003_variable_rpm_motor1_variable_rpm_motor2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variable',
            name='error_altitud',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='rpm_motor1',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='rpm_motor2',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='rpm_motor3',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='rpm_motor4',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='temp_bateria',
        ),
    ]
