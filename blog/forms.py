from django import forms
from .models import Placas

class PlacasForms (forms.ModelForm):
    class Meta :
        model = Placas
        fields = [
            'nombre',
            'no_Cedula',
            'chasis',
            'noPlaca',
            'compania',
            'fechaOrden',
            'endoso',
            'FechaEndoso',
            'Estado',
            'cedula',
            'Comentario',

        ]
