# Generated by Django 4.1.3 on 2022-12-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documental',
            name='comentario',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='documental',
            name='episodios',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='documental',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='actor_principal',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='anio',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='comentario',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='actor_principal',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='comentario',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='genero',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='serie',
            name='temporadas',
            field=models.IntegerField(null=True),
        ),
    ]
