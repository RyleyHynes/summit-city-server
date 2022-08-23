# Generated by Django 4.1 on 2022-08-23 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summitapi', '0002_remove_summituser_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='climb',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='climbs', to='summitapi.summituser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hike',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='hikes', to='summitapi.summituser'),
            preserve_default=False,
        ),
    ]
