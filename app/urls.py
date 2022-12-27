from django.urls import path
from app import views

urlpatterns=[

path('', views.inicio, name="inicio"),
path('busqueda', views.busqueda, name="busqueda"),
path('buscarpeli',views.buscarpeli, name="buscarpeli"),
path('buscarserie',views.buscarserie, name="buscarserie"),
path('buscardocumental',views.buscardocumental, name="buscardocumental"),


path('peliculas/',views.peliculas.as_view(), name="peliculas"),
path('peliculas/<pk>', views.peliculasdetalle.as_view(), name= "peliculasdetalle"),
#path('eliminarpelicula/<id>',views.eliminarpelicula.as_view(), name= "eliminarpelicula"),


path('series/', views.series.as_view(), name="series"),
path('series/detalle/<pk>', views.seriesdetalle.as_view(), name="seriesdetalle"),

path('documentales/', views.documentales.as_view(), name="documentales"),
path('documentales/<pk>', views.DocumentalDetalle.as_view(), name="documentalesdetalle"),


path('cargarpelis/', views.CargarPeliculas, name="CargarPeliculas"),
path('cargarseries/', views.CargarSeries, name= "CargarSeries"),
path('cargardocumentales/', views.CargarDocumentales, name="CargarDocumentales"),
]