# Generated by Django 2.2 on 2020-11-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0015_auto_20201110_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_context',
            field=models.TextField(blank=True, null=True),
        ),
    ]
