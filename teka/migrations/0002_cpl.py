# Generated by Django 3.2.7 on 2021-09-20 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=256, unique=True, verbose_name='CPL Name')),
                ('language', models.CharField(max_length=2, verbose_name='Language')),
                ('subtitles', models.CharField(blank=True, max_length=2, null=True)),
                ('runtime', models.IntegerField()),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('CPL', models.TextField()),
                ('KDM', models.TextField(blank=True, null=True)),
                ('encoded', models.BooleanField(default=False)),
                ('_key', models.BigIntegerField(blank=True, null=True)),
                ('_zip', models.BinaryField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teka.movie')),
            ],
        ),
    ]
