from django.urls import path
from app import views

urlpatterns=[

path('', views.inicio, name="inicio"),
path('perfil',views.perfil, name="perfil"),
path('iniciousuarios',views.iniciousuarios, name="iniciousuarios"),
path('busqueda', views.busqueda, name="busqueda"),
path('buscarpeli',views.buscarpeli, name="buscarpeli"),
path('buscarserie',views.buscarserie, name="buscarserie"),
path('buscardocumental',views.buscardocumental, name="buscardocumental"),
path('paginas/', views.paginas, name="paginas"),
path('about/', views.about, name="about"),


path('peliculas/',views.peliculas.as_view(), name="peliculas"),
path('peliculas/<pk>', views.peliculasdetalle.as_view(), name= "peliculasdetalle"),
path('peliculas/eliminar/<pk>',views.peliculaeliminar.as_view(), name= "pelicula.eliminar"),
path('peliculas/editar/<pk>', views.peliculaeditar.as_view(), name= "pelicula.editar"),


path('series/', views.series.as_view(), name="series"),
path('series/<pk>', views.seriesdetalle.as_view(), name="seriesdetalle"),
path('series/editar/<pk>', views.serieseditar.as_view(), name= "series.editar"),
path('series/eliminar/<pk>', views.serieseliminar.as_view(), name= "series.eliminar"),

path('documentales/', views.documentales.as_view(), name="documentales"),
path('documentales/<pk>', views.DocumentalesDetalle.as_view(), name="documentalesdetalle"),
path('documentales/editar/<pk>', views.documentaleseditar.as_view(), name= "documentales.editar"),
path('documentales/eliminar/<pk>', views.documentaleseliminar.as_view(), name= "documentales.eliminar"),

path('cargardocumentales/', views.CargarDocumentales, name="CargarDocumentales"),
path('cargarpelis/', views.CargarPeliculas, name="CargarPeliculas"),
path('cargarseries/', views.CargarSeries, name= "CargarSeries"),
]