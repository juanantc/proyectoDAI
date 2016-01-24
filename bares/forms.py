# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from bares.models import Tapas

class login_form(forms.ModelForm):
	username = forms.SlugField (max_length=8,
	                             label='Usuario')
	password = forms.SlugField (max_length=8,
	                        widget=forms.PasswordInput(),
	                        label='Contraseña')
	class Meta:
		model  = User
		fields = ('username', 'password')

class register_form(forms.ModelForm):
	username = forms.SlugField (max_length=8, label='Usuario')
	email    = forms.EmailField (label='Email')
	password = forms.SlugField (max_length=8,
	                   widget=forms.PasswordInput(),
	                   label='Contraseña')
	class Meta:
		model  = User
		fields = ('username', 'email', 'password')

class add_tapa_form(forms.ModelForm):
	nombre_tapa = forms.CharField(max_length=30, label='Nueva tapa')

	class Meta:
		model = Tapas
		fields = ('nombre_tapa',)
