# Generated by Django 2.0 on 2018-03-27 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20180327_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='user',
        ),
    ]
