from django.shortcuts import render
from  django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from appa.forms import *
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "app/inicio_usuarios.html", {"mensaje":f"usuario {username} creado correctamente"})
        else:
            return render(request,"appa/register.html", {"form": form, "mensaje":"error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "appa/register.html", {"form":form})

def login_usuario(request):
    if request=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario = authenticate(username=usu, password=clave)#verifica que el usuario exista en la base de dato. no loguea
            if usuario is not None:
                login(request,usuario)
                return render(request, "app/inicio_usuarios.html", {"mensaje":f"usuario {usu} logueado correctamente"})
            else:
                return render(request, "appa/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta"})
        else:
            return render(request, "appa/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta"})
    else:
        form=AuthenticationForm()
        return render(request, "appa/login.html", {"form":form})

