from django.db import models
from django.db.models.loading import load_app

class Entidad(models.Model):
    """Representa un departamento u otra institucion
    de la Universidad"""
    codigo = models.CharField(max_length = 10, blank = True, help_text = 'Si no es\
    un departamento de la universidad, deje este campo en blanco.')
    nombre = models.CharField(max_length = 60, unique = True)
    direccion = models.CharField(max_length = 120)

    def __unicode__(self):
        return self.nombre

class Materia(models.Model):
    """Identifica una materia"""
    codigo = models.CharField(max_length = 6, unique = True)
    nombre = models.CharField(max_length = 50)
    dpto = models.ForeignKey(Entidad)

    def __unicode__(self):
        return '(%s) %s' % (self.codigo, self.nombre)

class Profesor(models.Model):
    """Contiene los datos de un profesor registrado en el 
    sistema"""
    ci = models.IntegerField(max_length = 8, unique = True)
    nombre = models.CharField(max_length = 50)
    telefono = telefono = models.CharField(blank=True, help_text='Debe\
    estar en formato XXXX-XXXXXXX o XXXXXXX', max_length=12)
    email = models.EmailField()
    oficina = models.CharField(max_length = 50, blank = True)
    
    def __unicode__(self):
        return 'Prof. %s' % (self.nombre)

class Encargado(models.Model):
    """Contiene la informacion sobre el encargado de un curso.
    Esta tabla surge de la necesidad de diferenciar las personas 
    que son encargadas de un curso (estrictamente profesores) y 
    las personas que dictan el curso (preparadores, profesores, 
    ayudantes academicos, etc)."""
    profesor = models.ForeignKey(Profesor)
    dpto = models.ForeignKey(Entidad)
    
    def __unicode__(self):
        return 'Prof. %s/ Entidad: %s' % (self.profesor.nombre, self.departamento)
