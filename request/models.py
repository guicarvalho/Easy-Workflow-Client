# coding: utf-8

from django.db import models
from profile_user.models import UserProfile

class Request(models.Model):
    STATES_OF_REQUEST = (
        ('pending', 'Pendente'),
        ('realized', 'Realizada'),
        ('canceled', 'Cancelada'),
        ('delayed', 'Atrasada'),
    )

    LEVELS_OF_PRIORITY = (
        ('low', 'Baixa'),
        ('medium', u'Médio'),
        ('high', 'Alta'),
    )

    response = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    equipment = models.CharField(max_length=128)
    nature = models.CharField(max_length=128)
    status = models.CharField(max_length=12, choices=STATES_OF_REQUEST)
    priority = models.CharField(max_length=12, choices=LEVELS_OF_PRIORITY)
    who_requested = models.CharField(max_length=180)
    who_executed = models.CharField(max_length=180)