# coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Request


class RequestForm(forms.ModelForm):

	who_requested = forms.ChoiceField()
	who_executed = forms.ChoiceField()

	def __init__(self, who_requested, who_executed, *args, **kwargs):
		super(RequestForm, self).__init__(*args, **kwargs)

		self._populate_choice_field(who_requested, who_executed)
		self.fields['who_requested'].initial = (0, '--------')
		self.fields['who_executed'].initial = (0, '--------')

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

	def _populate_choice_field(self, who_requested, who_executed):
		list_who_requested = [(0, '--------')]
		list_who_executed = [(0, '--------')]

		for item in who_requested:
			
			if type(item) is tuple and len(item) == 2:
				list_who_requested.append(item)

			elif len(who_requested) == 2 and type(who_requested) is tuple:
				list_who_requested.append(who_requested)

		for item in who_executed:
			
			if type(item) is tuple and len(item) == 2:
				list_who_executed.append(item)

			elif len(who_executed) == 2 and type(who_executed) is tuple:
				list_who_executed.append(who_executed)

		self.fields['who_requested'].choices = list_who_requested
		self.fields['who_executed'].choices = list_who_executed