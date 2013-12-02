from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
	firstName = models.TextField(help_text="Nombre")
	lastName = models.TextField(help_text="apellidos")
	tipo_documento = models.TextField(help_text="tipo de documento")
	cc = models.TextField(help_text="numero de documento" unique = True)
	prioridad = models.TextField(help_text="Nombre")
	tiempo_ingreso = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.firstName