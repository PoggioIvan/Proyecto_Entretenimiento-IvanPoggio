# Generated by Django 4.1.3 on 2023-01-19 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_documental_episodios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documental',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='pelicula',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='autor',
        ),
    ]
