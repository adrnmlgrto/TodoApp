# Generated by Django 4.1.7 on 2023-02-26 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_remove_task_task_desc_task_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True),
        ),
    ]
