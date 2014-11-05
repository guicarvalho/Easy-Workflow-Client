# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = UserProfile
		fields = ['username', 'password', 'first_name', 'last_name', 'email', 'protocol', 'fone_number', 'cel_number', 'role']
		labels = {
			'username': 'Username',
			'password': 'Password',
			'first_name': 'First Name',
			'last_name': 'Last Name',
			'email': 'Email',
			'protocol': 'Protocol',
			'fone_number': 'Phone Number',
			'cel_number': 'Cell Phone Number',
			'Role': 'role',
		}