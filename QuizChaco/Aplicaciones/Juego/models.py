from django.db import models
from django.db.models.base import Model

# Create your models here.

class pregunta(models.Model):
	texto = models.CharField(max_length=200)
	puntos = models.PositiveSmallIntegerField(default=1)
	categoria = models.ForeignKey('categoria', on_delete=models.CASCADE)

	def __str__(self):
		return self.texto

	def get_answsers(self):
		return self.pregunta.all()

class respuesta(models.Model):
	texto = models.CharField(max_length=200)
	correcta = models.BooleanField(default=False)
	pregunta = models.ForeignKey('pregunta', on_delete=models.CASCADE)

	def __str__(self):
		return self.texto


class categoria(models.Model):
	nombre = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.nombre