# -*- coding: utf-8 -*-

from django.db import models

class Entidad(models.Model):
    """Representa un departamento u otra institución
    de la Universidad"""
    codigo = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.nombre

class Materia(models.Model):
    """Identifica una materia"""
    codigo = models.CharField(max_length = 6, primary_key = True)
    nombre = models.CharField(max_length = 50)
    departamento = models.ForeignKey(Entidad)

    def __unicode__(self): 
        return self.nombre

class Profesor(models.Model):
    """Contiene los datos de un profesor registrado en el 
    sistema"""
    cedula = models.IntegerField(primary_key = True)
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    email = models.EmailField()
    oficina = models.CharField(max_length = 50)
    departamento = models.ForeignKey(Entidad)
    
    def __unicode__(self):
        return u'%s/%s' % (self.nombre, self.departamento)

class Encargado(models.Model):
    """Contiene la información sobre el encargado de un curso.
    Esta tabla surge de la necesidad de diferenciar las personas 
    que son encargadas de un curso (estrictamente profesores) y 
    las personas que dictan el curso (preparadores, profesores, 
    ayudantes académicos, etc)."""
    profesor = models.ForeignKey(Profesor)
    departamento = models.ForeignKey(Entidad)

    def __unicode__(self):
        return self.profesor

