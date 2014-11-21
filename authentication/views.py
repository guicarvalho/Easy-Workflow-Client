# coding: utf-8

from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .exceptions import TokenEmptyException

import requests
import logging

logger = logging.getLogger(__name__)


class AuthenticationLoginView(TemplateView):
    
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super(AuthenticationLoginView, self).get_context_data(**kwargs)
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
                try:
                    data_user = self._get_user_informations(token, username)
                    request.session['token'] = token
                    request.session['username'] = data_user['username']
                    request.session['user'] = '%s %s' % (data_user['first_name'], data_user['last_name'])
                    request.session['role'] = data_user['role']

                except TokenEmptyException as e:
                    logger.error(str(e))

                except Exception as e:
                    logger.error(str(e))

                messages.success(request, 'Logged success!')

                return redirect(reverse('dashboard:home_page'), username=username)

        messages.error(request, 'Access danied!')

        return redirect(reverse('authentication:login'))


    def _get_user_informations(self, token, username):

        URL_GET_USERS = 'http://localhost:8001/users/%s' % username
        data_user_json = {}

        if token:

            headers = {
                'content-type': 'application/json',
                'Authorization': 'Token %s' % token
            }

            response = requests.get(url=URL_GET_USERS, headers=headers)

            if response:
                data_user_json = response.json()
        
        else:
            raise TokenEmptyException('Token cannot be empty!')

        return data_user_json


class AuthenticationLogoutView(TemplateView):

    def get(self, request, *args, **kwargs):
        request.session.clear()
        return redirect(reverse('authentication:login'))