# Generated by Django 2.2 on 2020-11-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0008_auto_20201109_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]