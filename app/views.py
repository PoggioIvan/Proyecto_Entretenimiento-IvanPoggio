from django.shortcuts import render
from .models import *
from app.forms import *
from django.views.generic import ListView

# Create your views here.
def inicio(request):
    return render(request, "app/inicio.html")

class peliculas(ListView):
    model=peliculas 
    template_name= "app/peliculas.html"
class series(ListView):
    model=series
    template_name= "app/series.html"
class documentales(ListView):
    model=documental
    template_name="app/documental.html"

    
def CargarPeliculas(request):
    if request.method=="POST":
        form= PeliculasForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            genero=informacion["genero"]
            anio=informacion["anio"]
            actor_principal=informacion["actor principal"]
            comentario= informacion["comentario"]
            pelicula=peliculas(nombre=nombre, genero=genero, anio=anio, actor_principal=actor_principal, comentario=comentario)
            pelicula.save()
            return render(request, "app/peliculas.html", {"mensaje":"peli cargada correctamente"})
        else:
            return render(request, "app/cargarpeli.html", {"form":form, "mensaje":"info invalida"})
    else:
        formulario= PeliculasForm()
        return render (request, "app/cargarpeli.html", {"form": formulario})

def CargarSeries(request):
    if request.method=="POST":
        form= SeriesForm(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            nombre=info["nombre"]
            genero=info["genero"]
            temporadas=info["temporadas"]
            actor_principal=info["actor principal"]
            comentario=info["comentario"]
            serie=series(nombre=nombre, genero=genero, temporadas=temporadas, actor_principal=actor_principal, comentario=comentario)
            serie.save()
            return render(request, 'app/series.html' , {"mensaje":"serie cargada"})
        else:
            return render(request, 'app/cargarseries.html', {"form": form, "mensaje": "info invalida"})
    else:
        formulario=SeriesForm()
        return render(request, 'app/cargarseries.html', {"form": formulario})

def cargardocumentales(request):
    pass






