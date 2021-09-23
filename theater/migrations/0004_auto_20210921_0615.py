# Generated by Django 3.2.7 on 2021-09-21 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0003_auto_20210921_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='inst_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='screen',
            name='theater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theater.theater'),
        ),
    ]