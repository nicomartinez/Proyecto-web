from principal.models import Paciente
from django.shorcuts import render_to_response

def lista_pacientes(request):
	pacientes = Paciente.objects.all
	return render_to_response('lista.html', {'lista':pacientes})

def agregar_paciente(request):
    if request.method=='POST':
        formulario = PacienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = PacienteForm()
    return render_to_response('formulario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def modificar_paciente(request, cc):
	return 

def eliminar_paciente(request, cc):
	return


