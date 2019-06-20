from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuarios.models import User
from apps.usuarios.forms import RegistroForm
from django.urls import reverse_lazy
# Create your views here.

def index(request):
	return render(request, 'recicla/index.html')


def info(request):
	return render(request, 'recicla/informacion.html')


class RegistroUsuario(CreateView):
	model = User
	template_name = "recicla/registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('index:Menu')
