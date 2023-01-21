from django.urls import path
from appa.views import *
from django.contrib.auth.views import LogoutView

urlpatterns=[

path("register/", register, name="register"),
path("login/", login_usuario, name="login"),
path("logout/", LogoutView.as_view(), name="logout"),
path("avatar/",Avatar,name="avatar"),
path("Editar/",EditarPerfil, name="editar"),
path("agregaravatar/", agregaravatar, name="agregaravatar")
]