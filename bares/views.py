# -*- coding: utf-8 -*-

from django.shortcuts import render
from bares.models import Bares, Tapas
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .forms import login_form, register_form, add_tapa_form
from django.contrib.auth.models import User

def index(request):
	form = login_form()
	context = {'bares': Bares.objects.order_by('-visitas')}

	if request.method == 'POST':
		usuario = request.POST.get('username')
		passw = request.POST.get('password')
		user = authenticate(username=usuario, password=passw)

		if user is not None and user.is_active:
			login(request, user)

	if request.user.is_authenticated():
		context['mensaje'] =  u'Bienvenido %s' % (request.user)
	else:
		context['form'] = form

	return render (request, 'bares/index.html', context)

def salir(request):
	 logout(request)
	 return redirect('/bares/')

def registro(request):
	form = register_form()
	context = {'form': form}
	if request.method == 'POST':
		form = register_form(request.POST)
		if form.is_valid():
			usuario = request.POST.get('username')
			email = request.POST.get('email')
			passw = request.POST.get('password')

			user = User.objects.create_user(usuario,email,passw)
			user.save()

			return redirect('/bares/')

	return render (request, 'bares/registro.html', context)

def bar(request,id):

	if request.method == 'POST':
		if request.POST.get('nombre_tapa') is not None:
			bar = Bares.objects.get(id_bar=id)
			tapa = Tapas(bar = bar, nombre_tapa = request.POST.get('nombre_tapa'))
			tapa.save()
		else:
			id_tapa = request.POST.get('id_tapa')
			tapa = Tapas.objects.get(id_tapa=id_tapa)
			t = Tapas(id_tapa=tapa.id_tapa,bar = tapa.bar, nombre_tapa = tapa.nombre_tapa,votos=tapa.votos+1)
			t.save()

	form = add_tapa_form()
	context = {'form': form}

	try:
		bar = Bares.objects.get(id_bar=id)
		tapas = Tapas.objects.filter(bar=bar).order_by('-votos')

		b = Bares(id_bar = bar.id_bar, nombre_bar = bar.nombre_bar , direccion = bar.direccion,visitas=bar.visitas+1)
		b.save()

		context['bar'] = Bares.objects.get(id_bar=id)
		context['tapas'] = tapas

		# Datos para gráfica
		nombres_tapas = []
		votos_tapas = []

		for t in tapas:
			nombres_tapas.append(t.nombre_tapa.encode('utf-8'))
			votos_tapas.append(t.votos)


		context['nombres_tapas'] = nombres_tapas
		context['votos_tapas'] = votos_tapas

	except Bares.DoesNotExist:
		pass

	return render(request, 'bares/bar.html', context)
