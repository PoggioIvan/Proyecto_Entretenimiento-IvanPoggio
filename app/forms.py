from django import forms

class PeliculaForm(forms.Form):
    nombre= forms.CharField(label= "Nombre De La Pelicula", max_length=50)
    genero= forms.CharField(label= "Genero", max_length=20)
    comentario= forms.CharField(label="Comentario", max_length=500)
    estreno= forms.DateField(label="Fecha De Estreno")
    imagen=forms.ImageField(label="imagen")
    

class SerieForm(forms.Form):
    nombre= forms.CharField(label= "Nombre De La Serie",max_length=50)
    genero= forms.CharField(label= "genero", max_length=20)
    comentario= forms.CharField(label= "Comentario", max_length=500)
    estreno= forms.DateField(label="Fecha De Estreno")
    imagen=forms.ImageField(label="imagen")
    
  

class DocumentalForm(forms.Form):
    nombre= forms.CharField(label= "Nombre Del Documental" , max_length=50)
    comentario= forms.CharField(label="Comentario", max_length=500)
    estreno= forms.DateField(label="Fecha De Estreno")
    imagen=forms.ImageField(label="imagen")
    