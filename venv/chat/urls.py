from django.urls import path
from . import views

urlpatterns = [
    path('', views.nombre, name='nombre'),
    path('nombre', views.nombre, name='nombre'),
    path('mensajes', views.ver_mensajes, name='ver_mensajes'),
]