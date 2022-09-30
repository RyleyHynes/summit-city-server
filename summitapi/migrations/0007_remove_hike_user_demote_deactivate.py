# Generated by Django 4.1 on 2022-09-30 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summitapi', '0006_climbtag_hiketag_tag_remove_hike_attraction_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hike',
            name='user',
        ),
        migrations.CreateModel(
            name='Demote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approveUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firstapproved', to='summitapi.summituser')),
                ('demotedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demoted', to='summitapi.summituser')),
                ('secondApproveUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondapproved', to='summitapi.summituser')),
            ],
        ),
        migrations.CreateModel(
            name='Deactivate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approveUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='firstdeactiveapproved', to='summitapi.summituser')),
                ('deactivatedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deactivate', to='summitapi.summituser')),
                ('secondApproveUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seconddeactiveapproved', to='summitapi.summituser')),
            ],
        ),
    ]
