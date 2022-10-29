from django import forms
from .models import Operacion


class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion

        fields = ('tipo', 'cantidad', 'material')

        widgets = {
            #'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de operacion'}),
            #'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            # 'fecha': forms.TextInput(attrs={'class':'form-control'}),
            #'usuario': forms.TextInput(attrs={'class':'form-control'}),
        }
