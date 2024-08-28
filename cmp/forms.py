from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        exclude = ['um', 'fm', 'uc', 'fc']
        widgets = {'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
                   'direccion': forms.TextInput(attrs={'class': 'form-control'}),
                    'contacto': forms.TextInput(attrs={'class': 'form-control'}),
                    'telefono': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}), 
                   }
        
        def __init__(self, *arg, **kwargs):
            super().__Init__(*arg, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                })