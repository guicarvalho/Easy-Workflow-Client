# coding: utf-8

import json
import requests
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import UserProfileForm


class UserProfileView(FormView):
	template_name = 'profile_user/register.html'
	form_class = UserProfileForm
	success_url = reverse_lazy('dashboard:home_page')

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