from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Cancha(models.Model):
    SERVICIOS_CHOICES = (('Vestuario', 'Vestuario'),
              ('Iluminacion', 'Iluminacion'),
              ('Cesped Sintetico', 'Cesped Sintetico'))

    TIPO_CHOICES = (('11', '11'),
              ('7', '7'),
              ('5', '5'))

    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    servicios = MultiSelectField(choices=SERVICIOS_CHOICES)
    
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre