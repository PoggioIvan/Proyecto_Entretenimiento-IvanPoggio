from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)



class mensaje(models.Model):
   
    Receptor=models.ForeignKey(User, on_delete=models.CASCADE)
    Mensaje=models.CharField(max_length=400)
    Recibido=models.BooleanField()
    Mandado=models.DateTimeField(auto_now_add=True)

   

