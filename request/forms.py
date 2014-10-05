# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
	class Meta:
		model = Request
		fields = ['equipment', 'nature', 'status', 'priority', 'who_requested', 'who_executed', 'description']
		labels = {
			'description': 'Description',
			'equipment': 'Equipment',
			'nature': 'Nature',
			'status': 'Status',
			'priority': 'Priority',
			'who_requested': 'Who Requested',
			'who_executed': 'Who Executed',
		}