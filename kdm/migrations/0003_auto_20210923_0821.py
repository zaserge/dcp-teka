# Generated by Django 3.2.7 on 2021-09-23 05:21

from django.db import migrations, models
import kdm.models


class Migration(migrations.Migration):

    dependencies = [
        ('kdm', '0002_alter_kdm_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kdm',
            old_name='dual_projector',
            new_name='TDL',
        ),
        migrations.AlterField(
            model_name='kdm',
            name='date_end',
            field=models.DateTimeField(default=kdm.models._now_plus_one_day, verbose_name='End Key Validity'),
        ),
    ]
