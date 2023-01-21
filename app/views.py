from django.shortcuts import render
from app.models import *
from app.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import  UpdateView, DeleteView
from django.urls import reverse_lazy
from appa.views import Avatar


# Create your views here.

def inicio(request):
    return render(request, "app/inicio.html")

def iniciousuarios(request):
    return render(request,"app/inicio_usuarios.html", {"avatar": Avatar(request)} )

def perfil(request):
    return render(request,"app/perfil.html",{"avatar":Avatar(request)})

def busqueda(request):
    return render(request,"app/busqueda.html")

def about(request):
    return render(request, "app/about.html")

def paginas(request):
    return render(request,"app/paginas.html")

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

class peliculaeliminar(DeleteView):
    model = Pelicula
    success_url = reverse_lazy("peliculas")
    
class peliculaeditar(UpdateView):
    model = Pelicula
    success_url = reverse_lazy("peliculas")
    fields = ['nombre', 'genero', 'estreno', 'comentario', 'imagen']

def CargarPeliculas(request):
    if request.method=="POST":
        form= PeliculaForm(request.POST)

        if form.is_valid():
            informacion= form.cleaned_data
            nombre= informacion["nombre"]
            genero= informacion["genero"]
            estreno=informacion["Fecha De Estreno"]
            imagen=informacion["Imagen"]
            comentario= informacion["comentario"]
            Peliculas= Pelicula(nombre=nombre, genero=genero, estreno=estreno,imagen=imagen, comentario=comentario)
            Peliculas.save()
            return render(request, "app/CargarPeliculas.html", {"mensaje":"peli cargada correctamente"})
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

class serieseditar(UpdateView):
    model = Serie
    success_url= reverse_lazy("series")
    fields = ['nombre', 'genero', 'estreno', 'comentario', 'imagen']

class serieseliminar(DeleteView):
    model= Serie
    success_url = reverse_lazy("series")

def CargarSeries(request):
    if request.method=="POST":
        form= SerieForm(request.POST)

        if form.is_valid():
            info= form.cleaned_data
            nombre=info["nombre"]
            genero=info["genero"]
            comentario=info["comentario"]
            estreno=info["Fecha De Estreno"]
            imagen=info["Imagen"]
            Series=Serie(nombre=nombre, genero=genero,estreno=estreno , imagen=imagen, comentario=comentario)
            Series.save()
            return render(request, 'app/cargarseries.html' , {"mensaje":"serie cargada"})
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
            comentario=info["comentario"]
            estreno=info["Fecha De Estreno"]
            imagen=info["Imagen"]
            Documentales= Documental(nombre= nombre, estreno=estreno,imagen=imagen, comentario= comentario)
            Documentales.save()
            return render(request, 'app/cargardocumentales.html',{"mensaje":"documental cargado"})
        else:
            return render(request, 'app/cargardocumentales.html', {"form": form, "mensaje":"info invalida"})
    else:
        formulario=DocumentalForm()
        return render(request, 'app/cargardocumentales.html', {"form": formulario})


class documentales(ListView):
    model=Documental
    template_name="app/documental_list.html"

class DocumentalesDetalle(DetailView):
    model=Documental
    template_name="app/documental_detalle.html"

class documentaleseliminar(DeleteView):
    model = Documental
    success_url = reverse_lazy("documentales")

class documentaleseditar(UpdateView):
    model= Documental
    success_url = reverse_lazy("documentales")
    fields = ['nombre', 'comentario', 'estreno','imagen']




