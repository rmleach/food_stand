# Generated by Django 2.1.7 on 2019-04-15 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distros', '0004_auto_20190415_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
