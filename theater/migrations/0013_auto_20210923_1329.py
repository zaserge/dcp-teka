# Generated by Django 3.2.7 on 2021-09-23 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0012_auto_20210923_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projector',
            old_name='certificate',
            new_name='icp_certificate',
        ),
        migrations.AddField(
            model_name='projector',
            name='ld_certificate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mediaserver',
            name='model',
            field=models.ForeignKey(blank=True, limit_choices_to={'field': 'mediaserver.model'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='model', to='theater.vars', verbose_name='Mediaserver Model'),
        ),
        migrations.AlterField(
            model_name='mediaserver',
            name='vendor',
            field=models.ForeignKey(blank=True, limit_choices_to={'field': 'mediaserver.vendor'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vendor', to='theater.vars', verbose_name='Mediaserver Vendor'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='mediaserver_pri',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mediaserver_pri', to='theater.mediaserver', verbose_name='Primary mediaserver'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='mediaserver_sec',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mediaserver_sec', to='theater.mediaserver', verbose_name='Secondary mediaserver'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='projector_pri',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projector_pri', to='theater.projector', verbose_name='Primary projector'),
        ),
        migrations.AlterField(
            model_name='screen',
            name='projector_sec',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projector_sec', to='theater.projector', verbose_name='Secondary projector'),
        ),
    ]
