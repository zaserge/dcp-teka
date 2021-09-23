# Generated by Django 3.2.7 on 2021-09-21 02:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0002_alter_theater_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaserver',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='projector',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='screen',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
