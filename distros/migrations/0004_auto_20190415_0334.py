# Generated by Django 2.1.7 on 2019-04-15 03:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('distros', '0003_auto_20190405_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.IntegerField(default=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='lng',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
