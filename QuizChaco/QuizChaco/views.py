from django import template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
#from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render
def saludo(request):

    documento="<html><body><h1>Hola alumnos, es la primera página con DJango<html><body><h1>"
    return HttpResponse(documento)
def despedida(request):
    return HttpResponse("Hasta luego alumnos!")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    <html>
    <body>
    <h1>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, anio):
    edadActual=18
    perdiodo=anio-2021
    edadFutura=edadActual+perdiodo
    documento="<html><body><h1>En el año %s tendras %s años <html><body><h1>" %(anio, edadFutura)

    return HttpResponse(documento)

def plantillaUno(request):
    #abre el documento que contiene la plantilla
    plantillaExterna = open("H:/ProyectoJuegoChaco/QuizChaco/QuizChaco/templates/plantillaUno.css")
    #carga el documento en una variable tipo 'Template'
    template = Template(plantillaExterna.read())
    #cierra el documento externo antes abierto
    plantillaExterna.close()
    #crear un contexto
    contexto = Context()
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaPreguntasUno(request):
    #abre el documento que contiene la plantilla
    plantillaExterna = open("H:/ProyectoJuegoChaco/QuizChaco/QuizChaco/templates/plPreguntaUno.html")
    #carga el documento en una variable tipo 'Template'
    template = Template(plantillaExterna.read())
    #cierra el documento externo antes abierto
    plantillaExterna.close()
    #crear un contexto
    contexto = Context()
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def pregunta(request):
    plantillaPreguntas = open("H:/ProyectoJuegoChaco/QuizChaco/QuizChaco/templates/plantillaPreguntas.html")
    template = Template(plantillaPreguntas.read())
    plantillaPreguntas.close()
    return HttpResponse(template)

def pantallaIndex(request):
    #abre el documento que contiene la plantilla
    plantillaIndex = open("H:/ProyectoJuegoChaco/QuizChaco/QuizChaco/templates/index.html")
    #carga el documento en una variable tipo 'Template'
    template = Template(plantillaIndex.read())
    #cierra el documento externo antes abierto
    plantillaIndex.close()
    #crear un contexto
    contexto = Context()
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaQuiz(request):
    #abre el documento que contiene la plantilla
    plantillaQuiz = open("H:/ProyectoJuegoChaco/QuizChaco/QuizChaco/templates/plantillaquiz.html")
    #carga el documento en una variable tipo 'Template'
    template = Template(plantillaQuiz.read())
    #cierra el documento externo antes abierto
    plantillaQuiz.close()
    #crear un contexto
    contexto = Context()
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def preguntaDos(request):
    #abre el documento que contiene la plantilla
    preguntaDos = open("H:/ProyectoJuegoChaco/QuizChaco/QuizChaco/templates/preguntasDos.html")
    #carga el documento en una variable tipo 'Template'
    template = Template(preguntaDos.read())
    #cierra el documento externo antes abierto
    preguntaDos.close()
    #crear un contexto
    contexto = Context()
    # Renderizar el documento:
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaCargador(request):
    plantillaExterna = get_template('plantillaQuiz.html')
    documento = plantillaExterna.render('plantillaQuiz.html')
    return HttpResponse(documento)

def plantillaShortcut(request):
    return render(request, 'plantillaQuiz.html', {})

def plantillaHija1(request):
    return render(request, 'plantillaHija_1.html', {})

def plantillaHija2(request):
    return render(request, 'plantillaHija_2.html', {})