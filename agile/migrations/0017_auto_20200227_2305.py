# Generated by Django 3.0.2 on 2020-02-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0016_auto_20200227_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_model',
            name='dateCompleted',
            field=models.DateField(),
        ),
    ]