# coding: utf-8

from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RequestForm


class RequestCreateView(CreateView):
	form_class = RequestForm
	template_name = 'request/register.html'