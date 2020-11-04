# Generated by Django 2.2 on 2020-11-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_auto_20201104_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('fulltime', 'Full Time'), ('parttime', 'Part Time'), ('remote', 'Remote')], max_length=1, null=True),
        ),
    ]