# Generated by Django 3.2.7 on 2021-09-21 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaServer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor', models.CharField(blank=True, max_length=64, null=True, verbose_name='Mediaserver Vendor')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='Mediaserver Model')),
                ('sw_ver', models.CharField(blank=True, max_length=64, null=True, verbose_name='Hardware/Software version')),
                ('serial', models.CharField(max_length=64, unique=True, verbose_name='Serial Number')),
                ('certificate', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projector',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor', models.CharField(blank=True, max_length=64, null=True, verbose_name='Projector Vendor')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='Projector Model')),
                ('sw_ver', models.CharField(blank=True, max_length=64, null=True, verbose_name='Hardware/Software version')),
                ('serial', models.CharField(max_length=64, unique=True, verbose_name='Serial Number')),
                ('certificate', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('name_int', models.CharField(blank=True, max_length=64, null=True)),
                ('circuit', models.CharField(blank=True, max_length=64, null=True)),
                ('street', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('state', models.CharField(blank=True, max_length=32, null=True)),
                ('postal', models.CharField(blank=True, max_length=16, null=True)),
                ('country', models.CharField(blank=True, max_length=8, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=64, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=64, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('timezone', models.CharField(default='current timezone', max_length=64)),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Comments')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Screen name/number')),
                ('audio_type', models.CharField(blank=True, max_length=32, null=True)),
                ('motin_fx', models.CharField(blank=True, max_length=32, null=True)),
                ('aspect_ratio', models.CharField(blank=True, max_length=32, null=True)),
                ('screen_mask', models.CharField(blank=True, max_length=32, null=True)),
                ('s3d_type', models.CharField(blank=True, max_length=32, null=True)),
                ('s3d_brightness', models.CharField(blank=True, max_length=32, null=True)),
                ('film_35mm', models.BooleanField(default=False)),
                ('integrator', models.CharField(blank=True, max_length=32, null=True)),
                ('inst_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mediaserver_pri', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mediaserver_pri', to='theater.mediaserver', verbose_name='Primary mediaserver')),
                ('mediaserver_sec', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mediaserver_sec', to='theater.mediaserver', verbose_name='Secondary mediaserver')),
                ('projector_pri', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projector_pri', to='theater.projector', verbose_name='Primary projector')),
                ('projector_sec', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projector_sec', to='theater.projector', verbose_name='Secondary projector')),
                ('theater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='theater.theater')),
            ],
        ),
    ]
