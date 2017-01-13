from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView 

from mundoDeportivo.models import *
from django.http.response import HttpResponse
from django.db.models.query import QuerySet

# Create your views here.


def noticias(request, pk=None, *args, **kwargs):
    
    equipo = get_object_or_404(Equipo, id=pk)
    noticias = Noticia.objects.filter(nombreEquipo=equipo)
    
    template = "noticias.html"
    context = {
        'queryset':noticias,
        'nombreEquipo':equipo,
    }
    
    return render(request,template,context)


def equipo(request):
    aux = Equipo.objects.filter()
    
    template = "equipos.html"
    
    context = {
        'nombreEquipo' : aux,
    }
    return render(request,template,context)

