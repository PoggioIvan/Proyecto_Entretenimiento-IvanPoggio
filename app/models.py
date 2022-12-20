from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre= models.CharField(max_length=50)
    genero= models.CharField(max_length=20)
    anio= models.IntegerField()
    actor_principal= models.CharField(max_length=40)
    comentario= models.CharField(max_length=500)
   

class Serie(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=20)
    temporadas= models.IntegerField()
    actor_principal= models.CharField(max_length=40)
    comentario= models.CharField(max_length=500)
    def __str__(self):
        return f"{self.nombre} {self.genero}"

class Documental(models.Model):
    nombre= models.CharField(max_length=50)
    episodios= models.IntegerField()
    comentario= models.CharField(max_length=500)
    def __str__(self):
        return f"{self.nombre}"
    
