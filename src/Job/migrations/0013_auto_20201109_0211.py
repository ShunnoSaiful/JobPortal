# Generated by Django 2.2 on 2020-11-09 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0012_auto_20201108_0941'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='user',
            new_name='company',
        ),
    ]