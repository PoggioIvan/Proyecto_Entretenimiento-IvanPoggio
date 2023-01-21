from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio


class EditarForm(UserCreationForm):
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Cambiar Contrasena", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar Contrasena", widget=forms.PasswordInput)

    class meta:
        model=User
        fields=["first_name","last_name","email", "password1","password2"]
        help_texts = {k:""  for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")
