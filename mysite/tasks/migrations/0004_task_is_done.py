# Generated by Django 3.2.9 on 2024-04-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
