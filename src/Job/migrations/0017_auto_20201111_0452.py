# Generated by Django 2.2 on 2020-11-11 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0016_auto_20201111_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='additional_req',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='application_procedure',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='compensation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='educational_req',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='experience_req',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_responsibility',
            field=models.TextField(blank=True, null=True),
        ),
    ]