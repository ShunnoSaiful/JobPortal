# Generated by Django 2.2 on 2020-11-09 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0008_auto_20201108_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_password',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_employee',
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]