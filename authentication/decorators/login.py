# coding: utf-8

from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def login_required(f):
    def wrap(request, *args, **kwargs):
        if 'token' not in request.session.keys():
            return redirect(reverse("authentication:login"))
        return f(request, *args, **kwargs)
    return wrap