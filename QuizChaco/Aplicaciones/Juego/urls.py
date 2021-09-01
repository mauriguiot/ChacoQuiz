from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juego/', views.iniciar_juego, name='juego')
]