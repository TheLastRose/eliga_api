# Generated by Django 3.0.2 on 2020-02-28 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0013_auto_20200227_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sprint_backlog',
            name='content',
        ),
    ]
