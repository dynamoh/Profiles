# Generated by Django 2.2 on 2019-08-11 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0009_auto_20190811_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
    ]
