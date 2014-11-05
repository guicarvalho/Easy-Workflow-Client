# coding: utf-8

from django.shortcuts import render
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import RequestForm

import json
import requests


class RequestCreateView(FormView):
	form_class = RequestForm
	template_name = 'request/register.html'
	success_url = reverse_lazy('dashboard:home_page')

	def form_valid(self, form):
		# import ipdb; ipdb.set_trace()
		equipment = form.cleaned_data.get('equipment')
		nature = form.cleaned_data.get('nature')
		status = form.cleaned_data.get('status')
		priority = form.cleaned_data.get('priority')
		who_requested = form.cleaned_data.get('who_requested')
		who_executed = form.cleaned_data.get('who_executed')
		description = form.cleaned_data.get('description')

		url = 'http://localhost:8001/requests/'

		credentials = [('username', 'guilherme'), ('password', 'teste')]
		
		payload = {
			'equipment': equipment,
			'nature': nature,
			'status': status,
			'priority': priority,
			'who_requested': who_requested,
			'who_executed': who_executed,
			'description': description
		}

		r = requests.post('http://localhost:8001/api-token-auth/', data=credentials)

		token = r.json().get('token')
		
		headers = {
			'content-type': 'application/json',
			'Authorization': 'Token %s' % token
		}

		r = requests.post(url=url, data=json.dumps(payload), headers=headers)

		return super(RequestCreateView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super(RequestCreateView, self).get_form_kwargs()

		who_executed = None
		
		url = 'http://localhost:8001/users/'

		credentials = [('username', 'guilherme'), ('password', 'teste')]

		r = requests.post('http://localhost:8001/api-token-auth/', data=credentials)

		token = r.json().get('token')

		headers = {
			'content-type': 'application/json',
			'Authorization': 'Token %s' % token
		}

		r = requests.get(url=url, headers=headers)			

		kwargs.update({
			'who_requested': self._get_executors(r.json()),
			'who_executed':  self._get_executors(r.json())
		})

		return kwargs

	def _get_executors(self, users_json):
		executors = []
		# import ipdb; ipdb.set_trace()

		for user in users_json:
			username = user.get('username')

			if username and username == 'guilherme': # mock logged user
				continue

			item = (user.get('id'), '%s %s' % (user.get('first_name'), user.get('last_name')))

			executors.append(item)

		return executors