# Generated by Django 2.0.2 on 2018-04-27 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('p_excel', '0004_auto_20180427_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('title', models.TextField()),
                ('untype', models.CharField(max_length=50)),
                ('patent', models.CharField(max_length=50)),
                ('classification', models.CharField(max_length=50)),
                ('inventor', models.CharField(max_length=50)),
                ('year_week', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Inventions1',
        ),
    ]
