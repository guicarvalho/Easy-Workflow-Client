# coding: utf-8

from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
import requests


class AuthenticationView(TemplateView):
    
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super(AuthenticationView, self).get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            url = 'http://localhost:8001/users/'

            credentials = [('username', username), ('password', password)]

            response = requests.post('http://localhost:8001/api-token-auth/', data=credentials)

            token = response.json().get('token')
            
            if token:
                request.session['token'] = token
                request.session['user'] = username

                messages.success(request, 'Logged success!')

                return render(request, 'dashboard/index.html',
                    {
                        'username': username
                    }
                )

        messages.error(request, 'Access danied!')

        return redirect(reverse('authentication:login'))
