# Generated by Django 4.1.3 on 2023-01-19 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appa', '0003_thread_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='created',
            new_name='Mandado',
        ),
        migrations.RemoveField(
            model_name='mensaje',
            name='thread',
        ),
        migrations.DeleteModel(
            name='Thread',
        ),
    ]
