from django import forms
from .models import Material, TipoMaterial


class TipoMaterialForm(forms.ModelForm):
    class Meta:
        model = TipoMaterial
        fields = '__all__'


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = '__all__'
        widgets = {
            # 'nombre':forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Nombre del Material', 'onFOcus':'validar{this}'}),
            'nombre': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'fecha': forms.DateField(),

        }
