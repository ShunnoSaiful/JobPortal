# Generated by Django 2.2 on 2020-11-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_auto_20201104_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('f', 'Full Time'), ('p', 'Part Time'), ('r', 'Remote')], max_length=1, null=True),
        ),
    ]
