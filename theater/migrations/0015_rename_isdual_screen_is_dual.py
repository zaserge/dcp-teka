# Generated by Django 3.2.7 on 2021-09-23 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0014_screen_isdual'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screen',
            old_name='isDual',
            new_name='is_dual',
        ),
    ]
