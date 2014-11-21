# coding: utf-8

from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

import requests
import logging

logger = logging.getLogger(__name__)


class HomePageView(TemplateView):
	
    def dispatch(self, request, *args, **kwrags):
        if 'token' not in request.session.keys():
            return redirect(reverse('authentication:login'))

        # get full name logged user
        full_name_logged_user = request.session.get('user')

        # get username logged user
        username = request.session.get('username')

        try:
            # get number and states of tasks of logged user
            user_tasks = self.__get_requests_logged_user(username)

            return render(request, 'dashboard/index.html', 
                {
                    'username': full_name_logged_user,
                    'realized_tasks': user_tasks['realized_tasks'],
                    'canceled_tasks': user_tasks['canceled_tasks'],
                    'pending_tasks': user_tasks['pending_tasks'],
                    'delayed_tasks': user_tasks['delayed_tasks']
                }
            )

        except Exception as e:
            logger.error(e)

        # TODO: redirect for page 500
        return render(request, 'dashboard/index.html') 


    def __get_requests_logged_user(self, username):

        realized_tasks = 0
        canceled_tasks = 0
        pending_tasks = 0
        delayed_tasks = 0

        try:
            url = 'http://localhost:8001/requests/%s/' % username
            r = requests.get(url).json()

            return dict(
                realized_tasks=r.get('realized'),
                canceled_tasks=r.get('canceled'),
                pending_tasks=r.get('pending'),
                delayed_tasks=r.get('delayed')
            )

        except Exception as e:
            logger.error('Error get number tasks of user. [ERROR]: %s' % e)
            raise e
