from django.shortcuts import render
from django.http import HttpResponse
from .models import respuesta, categoria

# Create your views here.

def inicio(request):
	return render(request, 'index.html')

def pregunta(request):
	pregunta = pregunta.objects.get(texto)
	return render(request, 'plPreguntaUno.html', {'pregunta': pregunta})

def opciones(request):
	opciones = respuesta.objects.all()
	return render(request, 'plPreguntaUno.html', {'opciones': opciones})