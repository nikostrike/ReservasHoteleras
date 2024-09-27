from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacion', 'fecha_inicio', 'fecha_fin', 'precio_total']
