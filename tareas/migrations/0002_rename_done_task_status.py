# Generated by Django 4.2.6 on 2023-10-16 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='done',
            new_name='status',
        ),
    ]
