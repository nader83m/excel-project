# Generated by Django 2.0.2 on 2018-05-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_excel', '0009_auto_20180427_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel_Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('filename', models.CharField(max_length=50)),
                ('year_week', models.CharField(max_length=50)),
            ],
        ),
    ]
