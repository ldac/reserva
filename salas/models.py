from django.db import models
from django.db.models.loading import load_app
from django.contrib.auth.models import User
#from reserva.reservas.models import Reservador
from reserva.universidad.models import Materia

OS_CHOICES = (
    ('l', 'GNU/Linux'),
    ('w', 'Windows XP'),
    ('a', 'Ambos'),
    )

SOLSOF_CHOICES = (
    ('A', 'Aceptado'),
    ('D', 'Denegado'),
    ('P', 'Pendiente'),
    )

class Software(models.Model):
    nombre = models.CharField(max_length=50)
    os = models.CharField(max_length=1, choices=OS_CHOICES)
    licencia = models.CharField(max_length=50, blank=True)
    website = models.URLField(max_length=300, blank=True)
    version = models.CharField(max_length=10, blank=True)
    descripcion = models.TextField(blank=True)
    #objects = SoftwareManager()

    def __unicode__(self):
        return '%s' % self.nombre

class Sala(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    direccion = models.CharField(max_length=7)
    reservable = models.BooleanField()
    privada = models.BooleanField()
    photo = models.ImageField(upload_to='images/salas/', blank=True)
    num_maquinas = models.PositiveIntegerField(max_length=2)
    software = models.ManyToManyField(Software)
    #objects = SalaManager()

    def __unicode__(self):
        return 'Sala %s' % self.nombre
    def software_linux(self):
        return self.software.filter(os='l')
    def software_windows(self):
        return self.software.filter(os='w')
    def software_both(self):
        return self.software.filter(os='a')

class Solicitud_Software(models.Model):
    """Contiene informacion sobre la solicitud 
    de un software en particular"""
    reservador = models.ForeignKey('reservas.Reservador')
    materia = models.ForeignKey(Materia)
    nombre = models.CharField(max_length = 50)
    os = models.CharField(max_length=1, choices=OS_CHOICES)
    licencia = models.CharField(max_length = 20)
    website = models.URLField(verify_exists = True)
    version = models.CharField(max_length = 10)
    descripcion = models.CharField(max_length = 100)
    status = models.CharField(max_length=1, choices=SOLSOF_CHOICES, default='P', blank=True)
    
    def __unicode__(self):
        return 'SOLICITUD_SOFTWARE: %s - %s' % (self.reservador, self.nombre)
    

class SalaManager(models.Manager):
    def obtener_reservables(self):
        return self.get_query_set().filter(reservable=True)

class SoftwareManager(models.Manager):
    def obtener_linux_software(self):
        return self.get_query_set().filter(os='l')

    def obtener_windows_software(self):
        return self.get_query_set().filter(os='w')

    def obtener_ambos_software(self):
        return self.get_query_set().filter(os='a')
