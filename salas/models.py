# -*- coding: utf-8 -*-

from django.db import models
from reservas.models import Reservador
from universidad.models import Materia

class Solicitud_Software(models.Model):
    """Contiene información sobre la solicitud 
    de un software en particular"""
    reservador = models.ForeignKey(Reservador)
    materia = models.ForeignKey(Materia)
    nombre = models.CharField(max_length = 50)
    sistema_op = models.CharField(max_length = 20)
    licencia = models.CharField(max_length = 20)
    website = models.URLField(verify_exists = True)
    version = models.CharField(max_length = 10)
    descripcion = models.CharField()
    status = models.CharField(max_length = 20)
    direccion_ip = models.IPAddressField()
