# coding: utf-8

from django.views.generic.base import TemplateView

from django.shortcuts import render


class HomePageView(TemplateView):

	template_name = 'dashboard/index.html'

	def get_context_data(self, **kwargs):
		context = super(HomePageView, self).get_context_data(**kwargs)
		return context