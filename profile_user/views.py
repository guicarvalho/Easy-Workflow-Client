# coding: utf-8

from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserProfileForm
from .models import UserProfile

class UserProfileCreateView(CreateView):
	form_class = UserProfileForm
	template_name = 'profile_user/register.html'

	print 'Passei aqui'