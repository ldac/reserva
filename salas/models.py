# -*- coding: utf-8 -*-

from django.db import models

class Solicitud_Software(models.Model):
    """Contiene información sobre la solicitud 
    de un software en particular"""
    reservador = models.ForeignKey(???)
    materia = models.ForeignKey(???)
    nombre = models.CharField()
    sistema_op = models.CharField()
    licencia = models.CharField()
    website = models.CharField()
    version = models.CharField()
    descripcion = models.CharField()
    status = models.CharField()
    direccion_ip = models.CharField()
