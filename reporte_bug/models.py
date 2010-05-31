# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.loading import load_app

BUG_STATUS = (
    ('P', 'Pendiente'),
    ('A', 'Arreglago'),
    ('I', 'Imposible'),
    )

class ReporteBug(models.Model):
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    reportador = models.ForeignKey(User, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, help_text=u'Si quiere recibir respuesta acerca del bug que esta posteando, puede dejarnos su email')    
    status = models.CharField(max_length=1, choices=BUG_STATUS, default='P')
    comentario = models.TextField(help_text=u'Por favor describa detalladamente el error. Si el error no lo vio en la pagina donde usted se encuentra actualmente, indiquelo.')
    respuesta = models.TextField(blank=True)
    resuelto = models.BooleanField(editable=False, default=False)

    def __unicode__(self):
        return "BUG: (%s) %s..." % (self.reportador, self.comentario[:10])
