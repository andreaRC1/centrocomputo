from django import forms
from .models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'tipo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo', 'require pattern': "[a-zA-Z ]{2,254}"}),
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca', 'require pattern': "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo', 'require pattern': "^\w+$"}),
            'disponibilidad': forms.Select(attrs={'class': 'forms-control'})
        }
