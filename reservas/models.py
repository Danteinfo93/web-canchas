from django.db import models
from canchas.models import Cancha
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Reserva(models.Model):
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE,)
    cliente = models.CharField(max_length=50)
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hs = models.DateTimeField()
    creacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['creacion']
    
    def __str__(self):
        return '%s %s' % (self.fecha_hs.strftime('%x - %X'), self.cancha)