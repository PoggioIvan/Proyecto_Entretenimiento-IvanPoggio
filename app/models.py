from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    genero = models.CharField(max_length=20, null=True)
    anio = models.IntegerField(null=True)
    actor_principal = models.CharField(max_length=40, null=True)
    comentario = models.CharField(max_length=500, null=True)
    def __str__(self):
        return f"{self.nombre} {self.genero}"
   

class Serie(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    genero = models.CharField(max_length=20, null=True)
    temporadas = models.IntegerField(null=True)
    actor_principal = models.CharField(max_length=40, null=True)
    comentario = models.CharField(max_length=500, null=True)
    def __str__(self):
        return f"{self.nombre} {self.genero}"
 

class Documental(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    episodios= models.IntegerField(null=True)
    comentario= models.CharField(max_length=200,null=True)
    def __str__(self):
        return f"{self.nombre}"
  
   
   
    
