# Generated by Django 2.2 on 2020-11-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0009_auto_20201109_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='emp_education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='emp_overview',
            field=models.TextField(blank=True, null=True),
        ),
    ]
