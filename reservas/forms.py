from django import forms
from .models import Reserva
import datetime

class ReservaModelForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ['cancha', 'cliente', 'fecha_hs']

    def clean_fecha_hs(self):
        fecha_hs = self.cleaned_data.get("fecha_hs")
        cancha = self.cleaned_data.get("cancha")
        fecha_hs_fin = fecha_hs + datetime.timedelta(hours=1) - datetime.timedelta(seconds=1)
        r_anterior = Reserva.objects.filter(cancha__exact=cancha).filter(fecha_hs__lt=fecha_hs).exclude(id=self.instance.id) #El exclude es para actualizar correctamente
        if r_anterior.exists():
            r_anterior = r_anterior.last()
            fh_anterior = r_anterior.fecha_hs + datetime.timedelta(hours=1)
            if fh_anterior > fecha_hs:
                raise forms.ValidationError("No hay disponibilidad este dia/hora: Solapamiento con reserva anterior.")
        if Reserva.objects.filter(cancha__exact=cancha).filter(fecha_hs__range=[fecha_hs, fecha_hs_fin ]).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("No hay disponibilidad este dia/hora:Solapamiento con reserva siguiente.")

        return fecha_hs

