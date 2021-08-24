"""QuizChaco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from QuizChaco.views import plantillaUno
from QuizChaco.views import plantillaPreguntasUno
from QuizChaco.views import pantallaIndex
from django.conf import settings
from django.conf.urls.static import static
from QuizChaco.views import plantillaQuiz
from QuizChaco.views import preguntaDos
from QuizChaco.views import plantillaCargador
from QuizChaco.views import plantillaShortcut
from QuizChaco.views import plantillaHija1
from QuizChaco.views import plantillaHija2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plantillaNumeroUno/', plantillaUno),
    path('plantillaPreguntasUno/', plantillaPreguntasUno),
    path('index/', pantallaIndex),
    path('quiz/', plantillaQuiz),
    path('preguntados/', preguntaDos),
    path('cargador/', plantillaCargador),
    path('shortcut/', plantillaShortcut),
    path('plantillaHija1/', plantillaHija1),
    path('plantillaHija2/', plantillaHija2),
]