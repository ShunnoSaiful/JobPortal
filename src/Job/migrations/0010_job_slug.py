# Generated by Django 2.2 on 2020-11-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0009_job_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
