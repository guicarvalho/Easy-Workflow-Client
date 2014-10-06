# coding: utf-8

from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import UserProfileForm

# fake
from django.contrib.auth import authenticate
import requests


class UserProfileCreateView(CreateView):
	form_class = UserProfileForm
	template_name = 'profile_user/register.html'
	success_url = reverse_lazy('dashboard:home_page')

	def post(self, request, *args, **kwargs):

		r = requests.get('http://localhost:8001/requests/', auth=('guilherme', 'teste'))

		print r.json()

		return HttpResponseRedirect(self.success_url)