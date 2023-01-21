from django.contrib import admin

from appa.models import avatar, mensaje
from .models import *

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Documental)
admin.site.register(avatar)
admin.site.register(mensaje)
