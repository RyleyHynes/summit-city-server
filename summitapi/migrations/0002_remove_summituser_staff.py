# Generated by Django 4.1 on 2022-08-21 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summitapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summituser',
            name='staff',
        ),
    ]
