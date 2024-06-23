from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensajes

def nombre(request):
    return HttpResponse("<h1>CITLALLI MARÍN RODRÍGUEZ</h1><h2><a href='mensajes'>Enlace a la vista de mensajes</a></h2>")

def ver_mensajes(request):
    mensajes = Mensajes.objects.all().order_by('id')
    return render(request, 'chat/ver_mensajes.html', {'mensajes': mensajes})