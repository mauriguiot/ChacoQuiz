from django.db import models
from django.db.models.base import Model

# Create your models here.
class Juego(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField