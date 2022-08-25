from django.shortcuts import render
from .models import Curso  
from django.http import HttpResponse




# Create your views here.
def curso(request):
    curso=Curso(nombre='Python',comision=31105)
    curso.save()
    texto=f'Curso creado: nombre: {curso.nombre} comision: {curso.comision}'
    return HttpResponse(texto)

