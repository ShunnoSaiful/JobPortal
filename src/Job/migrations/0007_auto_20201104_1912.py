# Generated by Django 2.2 on 2020-11-04 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0006_auto_20201104_1852'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='company',
            new_name='user',
        ),
    ]
