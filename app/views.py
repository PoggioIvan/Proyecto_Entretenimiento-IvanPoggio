from django.shortcuts import render
from app.models import *
from app.forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
def inicio(request):
    return render(request, "app/inicio.html")

def busqueda(request):
    return render(request,'app/busqueda.html')


def buscarpeli(request):
        nombre=request.GET["nombre"]
        if nombre!="":
            peliculas=Pelicula.objects.filter(nombre__icontains=nombre)
            return render(request, "app/resultadosbusqueda1.html", {"peliculas":peliculas, "nombre":nombre})
        else:
            return render(request,"app/busqueda.html", {"mensaje": "ingresa un nombre"})

def buscarserie(request):
        nombre=request.GET["nombre"]
        if nombre!="":
            serie=Serie.objects.filter(nombre__icontains=nombre)
            return render(request, "app/resultadosbusqueda2.html", {"serie":serie, "nombre":nombre})
        else:
            return render(request,"app/busqueda.html", {"mensaje": "ingresa un nombre"})


def buscardocumental(request):
        nombre=request.GET["nombre"]
        if nombre!="":
            documental=Documental.objects.filter(nombre__icontains=nombre)
            return render(request, "app/resultadosbusqueda3.html", {"documental":documental, "nombre":nombre})
        else:
            return render(request,"app/busqueda.html", {"mensaje": "ingresa un nombre"})
        

class peliculas(ListView):
    model=Pelicula 
    template_name= "app/peliculas_list.html"

class peliculasdetalle(DetailView):
    model=Pelicula
    template_name= "app/pelicula_detalle.html"

class eliminarpelicula(DetailView):
    pass

def CargarPeliculas(request):
    if request.method=="POST":
        form= PeliculaForm(request.POST)

        if form.is_valid():
            informacion= form.cleaned_data
            nombre= informacion["nombre"]
            genero= informacion["genero"]
            anio= informacion["anio"]
            actor_principal= informacion["actor_principal"]
            comentario= informacion["comentario"]
            Peliculas= Pelicula(nombre=nombre, genero=genero, anio=anio, actor_principal=actor_principal, comentario=comentario)
            Peliculas.save()
            return render(request, "app/peliculas_list.html", {"mensaje":"peli cargada correctamente"})
        else:
            return render(request, "app/CargarPeliculas.html", {"form":form, "mensaje":"info invalida"})
    else:
        formulario= PeliculaForm()
        return render (request, "app/CargarPeliculas.html", {"form": formulario})

#............................................................................................................................................
class series(ListView):
    model=Serie
    template_name= "app/series_list.html"

class seriesdetalle(DetailView):
    model= Serie
    template_name= "app/series_detalle.html"

def CargarSeries(request):
    if request.method=="POST":
        form= SerieForm(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            nombre=info["nombre"]
            genero=info["genero"]
            temporadas=info["temporadas"]
            actor_principal=info["actor_principal"]
            comentario=info["comentario"]
            Series=Serie(nombre=nombre, genero=genero, temporadas=temporadas, actor_principal=actor_principal, comentario=comentario)
            Series.save()
            return render(request, 'app/series_list.html' , {"mensaje":"serie cargada"})
        else:
            return render(request, 'app/cargarseries.html', {"form": form, "mensaje": "info invalida"})
    else:
        formulario=SerieForm()
        return render(request, 'app/cargarseries.html', {"form": formulario})
#.........................................................................................................................................

def CargarDocumentales(request):
    if request.method=="POST":
        form= DocumentalForm(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            nombre=info["nombre"]
            episodios=info["episodios"]
            comentario=info["comentario"]
            Documentales= Documental(nombre= nombre, episodios= episodios, comentario= comentario)
            Documentales.save()
            return render(request, 'app/documental_list.html',{"mensaje":"documental cargado"})
        else:
            return render(request, 'app/cargardocumentales.html', {"form": form, "mensaje":"info invalida"})
    else:
        formulario=DocumentalForm()
        return render(request, 'app/cargardocumentales.html', {"form": formulario})


class documentales(ListView):
    model=Documental
    template_name="app/documental_list.html"

class DocumentalDetalle(DetailView):
    model=Documental
    template_name="app/documental_detalle.html"

#cuando cree los usuarios tengo que poner que la navbar si no estas registrado no muestre nada solo registrarce 
# y que esa pagina tenga una lista con todas las series peliculas y documentales que hay 


