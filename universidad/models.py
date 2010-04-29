from django.db import models

# Create your models here.

class Entidad(models.Model):
    """Representa un departamento u otra institución
    de la Universidad"""
    codigo = models.CharField()
    nombre = models.CharField()
    direccion = models.CharField()

    def __unicode__(self):
        return self.nombre

class Materia(models.Model):
    """Identifica una materia"""
    codigo = models.CharField(max_length = 6, primary_key = True)
    nombre = models.CharField()
    departamento = models.ForeignKey(Entidad)

    def __unicode__(self): 
        return self.nombre

class Profesor(models.Model):
    """Contiene los datos de un profesor registrado en el 
    sistema"""
    cedula = models.CharField(max_length = 9, primary_key = True)
    nombre = models.CharField()
    telefono = models.CharField()
    email = models.CharField()
    oficina = models.CharField()
    departamento = models.ForeignKey(Entidad)
    
    def __unicode__(self):
        return self.nombre + '/' + self.departamento

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

