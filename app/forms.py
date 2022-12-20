from django import forms

class PeliculasForm(forms.Form):
    nombre: forms.CharField(label= "Nombre De La Pelicula", max_length=50)
    genero: forms.CharField(label= "Genero", max_length=20)
    anio: forms.IntegerField()
    actor_principal: forms.CharField(label="Actor Principal", max_length=40)
    comentario: forms.CharField(label="Comentario", max_length=500)


class SeriesForm(forms.Form):
    nombre:forms.CharField(label= "Nombre De La Serie",max_length=50)
    genero:forms.CharField(label= "genero", max_length=20)
    temporadas: forms.IntegerField()
    actor_principal: forms.CharField(label="Actor Principal", max_length=40)
    comentario: forms.CharField(label= "Comentario", max_length=500)

class DocumentalForm(forms.Form):
    nombre: forms.CharField(label= "Nombre Del Documental" , max_length=50)
    episodios: forms.IntegerField()
    comentario: forms.CharField(label="Comentario", max_length=500)
    