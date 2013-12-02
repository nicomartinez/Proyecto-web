#encoding:utf-8 
from django.forms import ModelForm
from principal.models import Paciente

class PacienteForm(ModelForm):
	class Meta:
		model = Paciente