# Generated by Django 2.2 on 2020-11-08 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0005_auto_20201108_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='company_username',
            new_name='user',
        ),
    ]
