from django.shortcuts import render
from  django.contrib.auth.forms import AuthenticationForm
from appa.forms import *
from django.contrib.auth import login, logout, authenticate
from appa.models import avatar
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method=="POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "app/inicio.html", {"mensaje":f"usuario {username} creado correctamente"})
        else:
            return render(request,"appa/register.html", {"form": form, "mensaje":"error al crear el usuario"})
    else:
        form= RegistroUsuarioForm()
        return render(request, "appa/register.html", {"form":form})

def login_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario = authenticate(username=usu, password=clave)#verifica que el usuario exista en la base de dato. no loguea
            if usuario is not None:
                login(request,usuario)
                return render(request, "app/inicio_usuarios.html", {"mensaje":f"usuario {usu} logueado correctamente","avatar": Avatar(request)})
            else:
                return render(request, "appa/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta"})
        else:
            return render(request, "appa/login.html", {"form":form, "mensaje":"usuario o contraseña incorrecta"})
    else:
        form=AuthenticationForm()
        return render(request, "appa/login.html", {"form":form})

@login_required
def EditarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        formu=EditarForm(request.POST)
        if formu.is_valid():
            info=formu.cleaned_data
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.save()
            return render(request,"app/inicio_usuarios.html",{"mensaje":f"usuario{usuario.username} editado correctamente"})
        else:
            return render(request,"appa/editar.html",{"formu":formu,"nombreusuario":usuario.username})
    else:
        formu=EditarForm(instance=usuario)
        return render(request,"appa/editar.html",{"formu":formu, "nombreusuario":usuario.username})


def Avatar(request):
    lista=avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatars=lista[0].imagen.url
    else:
        avatars="/media/avatars/images.jpg"
    return avatars

def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST,request.FILES)
        if form.is_valid():
            avatars=avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarviejo=avatar.objects.filter(user=request.user)
            if len(avatarviejo)>0:
                avatarviejo[0].delete()
            avatars.save()
            return render(request, "appa/agregaravatar.html", {"mensaje":f"Avatar agregado"})
        else:
            return render(request, "appa/agragaravatar.html", {"fomr":form, "usuario":request.user, "mensaje":'Error al cargar el avatar'})
    else:
        form=AvatarForm()
        return render(request, "appa/agregaravatar.html", {"form": form, "usuario":request.user})