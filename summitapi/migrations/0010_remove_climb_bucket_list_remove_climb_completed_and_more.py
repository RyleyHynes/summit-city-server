# Generated by Django 4.1 on 2022-10-04 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summitapi', '0009_rename_tag_climb_tags_remove_climb_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='climb',
            name='bucket_list',
        ),
        migrations.RemoveField(
            model_name='climb',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='hike',
            name='bucket_list',
        ),
        migrations.RemoveField(
            model_name='hike',
            name='completed',
        ),
    ]