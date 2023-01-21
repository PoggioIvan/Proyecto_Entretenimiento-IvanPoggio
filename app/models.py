from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    genero = models.CharField(max_length=20, null=True)
    comentario = models.CharField(max_length=500, null=True)
    estreno=models.DateField(null=True)
    imagen=models.ImageField(upload_to="fotos",null=True)
    def __str__(self):
        return f"{self.nombre}"
    
   

class Serie(models.Model):
    nombre = models.CharField(max_length=50,null=True)
    genero = models.CharField(max_length=20, null=True)
    comentario = models.CharField(max_length=500, null=True)
    estreno=models.DateField(null=True)
    imagen=models.ImageField(upload_to="fotos",null=True)
    def __str__(self):
        return f"{self.nombre}"
 

class Documental(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    comentario= models.CharField(max_length=200,null=True)
    estreno= models.DateField(null=True)
    imagen=models.ImageField(upload_to="fotos",null=True)
    def __str__(self):
        return f"{self.nombre}"
  

   
   
    
