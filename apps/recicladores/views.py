from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
	return render(request, 'recicla/menu.html')

@login_required
def videos(request):
	return render(request, 'recicla/videos.html')


@login_required
def SolicitaAyudaa(request):
	return render(request, 'recicla/chat.html')


@login_required
def recicla1(request):
	return render(request, 'recicla/recicla1.html')

@login_required
def recicla2(request):
	return render(request, 'recicla/recicla2.html')

@login_required
def recicla3(request):
	return render(request, 'recicla/recicla3.html')

@login_required
def recicla4(request):
	return render(request, 'recicla/recicla4.html')

@login_required
def recicla5(request):
	return render(request, 'recicla/recicla5.html')

@login_required
def recicla6(request):
	return render(request, 'recicla/recicla6.html')

@login_required
def recicla7(request):
	return render(request, 'recicla/recicla7.html')

@login_required
def recicla8(request):
	return render(request, 'recicla/recicla8.html')