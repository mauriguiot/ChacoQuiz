from django.shortcuts import render
from django.http import HttpResponse
from .models import pregunta, respuesta, categoria

# Create your views here.

def inicio(request):
	return render(request, 'index.html')

def iniciar_juego(request):
	preguntas = pregunta.objects.all()
	opciones = respuesta.objects.all()
	return render(request, 'quiz.html', {'preguntas': preguntas, 'opciones': opciones})



# Esta función contabiliza la cantidad de respuestas correctas y devuelve la calificación

def show_result(request):
	respuestas_correctas = 0
	respuestas_incorrectas = 0
	puntos = 0

	while respuesta.objects.filter(correcta=True):
		respuestas_correctas = respuestas_correctas + 1
		puntos = puntos + pregunta.objets.all()

	while respuesta.objects.filter(correcta=False):
		respuestas_incorrectas = respuestas_incorrectas + 1

	return render(request, 'template.html', {'calificacion': puntos, 'correctas': respuestas_correctas, 
		'incorrectas': respuestas_incorrectas})


