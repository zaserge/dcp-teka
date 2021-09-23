# Generated by Django 3.2.7 on 2021-09-23 05:21

from django.db import migrations
import django.utils.timezone
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0006_auto_20210922_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theater',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(choices_display='WITH_GMT_OFFSET', default=django.utils.timezone.get_current_timezone),
        ),
    ]
