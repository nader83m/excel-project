# Generated by Django 2.0.2 on 2018-04-27 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('p_excel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipc_classification',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
