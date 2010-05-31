from django.db import models
from django.db.models.loading import load_app
from django.contrib.auth.models import User
from reserva.universidad.models import Entidad, Materia, Profesor, Encargado
#from reserva.salas.models import Sala

DIAS_SEMANA = (
    ('1', u'Lunes'),
    ('2', u'Martes'),
    ('3', u'Miercoles'),
    ('4', u'Jueves'),
    ('5', u'Viernes'),
    )

STATUS_SOLIC = (
    ('-1', 'Espera confirmacion'),
    ('0', 'Rechazada'),
    ('1', 'Aceptada'),
    ('2', 'Dudosa'),
    )

class Reservador(models.Model):
    djuser = models.ForeignKey(User, unique=True)
    ci = models.IntegerField(max_length=8, unique=True)
    entidad = models.ForeignKey(Entidad)
    oficina = models.CharField(max_length=15, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    super_reservador = models.BooleanField(default=False) # if True, puede reservar materias de cualquier departamento
    #objects = ReservadorManager()

    def __unicode__(self):
        return "%s" % self.djuser.username

class Reserva(models.Model):
    materia = models.ForeignKey(Materia)
    seccion = models.PositiveIntegerField(max_length=2)
    reservador = models.ForeignKey(Reservador)
    sala = models.ForeignKey('salas.Sala')
    profesor = models.ForeignKey(Profesor)
    encargado = models.ForeignKey(Encargado)
    trimestre = models.CharField(max_length=12)
    semana = models.PositiveIntegerField(max_length=2)
    dia = models.IntegerField(max_length=1, choices=DIAS_SEMANA)
    hora = models.PositiveIntegerField(max_length=2)
    fecha = models.DateTimeField(auto_now_add=True)
    #objects = ReservaManager()

    def obtener_dia(self):
        return WEEK_DAYS[self.dia - 1][1]

    def __unicode__(self):
        return '(%s) %s-Semana %s, Hora %s' % (self.trimestre, self.obtener_dia(), self.semana, self.hora)

class SolicitudPermiso(models.Model):
    ci = models.IntegerField(max_length=8, unique=True)
    login = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    entidad = models.ForeignKey(Entidad)
    oficina = models.CharField(max_length=15, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    email = models.EmailField(help_text=u'Se requiere que suministre un email valido, un mensaje de confirmacion sera enviado al mismo')
    comentario = models.TextField(blank=True)
    status = models.IntegerField(max_length=1, choices=STATUS_SOLIC, editable=False, default='-1')
    fecha = models.DateTimeField(auto_now_add=True)
    #objects = SolicitudPermisoManager()

    def __unicode__(self):
        return 'Solicitud %s' % self.login
