from django.urls import path
from app import views

urlpatterns=[

path('', views.inicio, name="inicio"),
path('peliculas/',views.peliculas.as_view(), name="peliculas"),
path('series/', views.series.as_view(), name="series"),
path('documentales/', views.documentales.as_view(), name="documentales"),
path('cargarpelis/', views.CargarPeliculas, name="CargarPeliculas"),
path('peliculas/detalle/', views.peliculasdetalle.as_view(), name= "peliculasdetalle"),
]