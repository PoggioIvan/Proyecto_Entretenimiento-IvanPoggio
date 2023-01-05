from django.urls import path
from appa.views import *

urlpatterns=[

path("register/", register, name="register"),
path("login/", login_usuario, name="login")
]