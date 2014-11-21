# coding: utf-8

from django.views.generic import FormView
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse, reverse_lazy

from .forms import UserProfileForm

from .models import UserProfile

import json
import requests


class UserProfileView(FormView):
	template_name = 'profile_user/register.html'
	form_class = UserProfileForm
	success_url = reverse_lazy('dashboard:home_page')


	def get_context_data(self, **kwargs):
		context = super(UserProfileView, self).get_context_data(**kwargs)
		context['username'] = self.request.session.get('user')
		
		return context


	def dispatch(self, request, *args, **kwargs):
		if 'token' not in request.session.keys():
			return redirect(reverse('authentication:login'))

		return super(UserProfileView, self).dispatch(request, *args, **kwargs)


	def form_valid(self, form):
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		first_name = form.cleaned_data.get('first_name')
		last_name = form.cleaned_data.get('last_name')
		email = form.cleaned_data.get('email')
		protocol = form.cleaned_data.get('protocol')
		fone_number = form.cleaned_data.get('fone_number')
		cel_number = form.cleaned_data.get('cel_number')
		role = form.cleaned_data.get('role')

		url = 'http://localhost:8001/users/'

		credentials = [('username', 'guilherme'), ('password', 'teste')]
		
		payload = {
			'username': username,
			'password': password,
			'first_name': first_name,
			'last_name': last_name,
			'email': email,
			'protocol': protocol,
			'fone_number': fone_number.replace('-', ''),
			'cel_number': cel_number.replace('-', ''),
			'role': role
		}

		r = requests.post('http://localhost:8001/api-token-auth/', data=credentials)

		token = r.json().get('token')
		
		headers = {
			'content-type': 'application/json',
			'Authorization': 'Token %s' % token
		}

		r = requests.post(url=url, data=json.dumps(payload), headers=headers)

		return super(UserProfileView, self).form_valid(form)


class UserProfileListView(ListView):
	template_name = 'profile_user/list.html'
	model = UserProfile
	# paginate_by = 10


	def get_context_data(self, **kwargs):
		context = super(UserProfileListView, self).get_context_data(**kwargs)
		context['username'] = self.request.session.get('user')

		return context


	def dispatch(self, request, *args, **kwargs):
		if 'token' not in request.session.keys():
			return redirect(reverse('authentication:login'))

		return super(UserProfileListView, self).dispatch(request, *args, **kwargs)


	def get_queryset(self):

		url = 'http://localhost:8001/users/'
		
		credentials = [('username', 'guilherme'), ('password', 'teste')]
		
		r = requests.post('http://localhost:8001/api-token-auth/', data=credentials)
		
		token = r.json().get('token')
		
		headers = {
			'content-type': 'application/json',
			'Authorization': 'Token %s' % token
		}
		
		r = requests.get(url=url, headers=headers)

		return r.json()