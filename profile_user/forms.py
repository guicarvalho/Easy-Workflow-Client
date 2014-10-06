# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
	error_css_class = 'alert alert-danger'
	email = forms.EmailField()

	class Meta:
		model = UserProfile
		fields = ['username', 'first_name', 'last_name', 'email', 'protocol', 'fone_number', 'cel_number', 'role']
		labels = {
			'username': 'Username',
			'first_name': 'First Name',
			'last_name': 'Last Name',
			'email': 'Email',
			'protocol': 'Protocol',
			'fone_number': 'Phone Number',
			'cel_number': 'Cell Phone Number',
			'Role': 'role',
		}