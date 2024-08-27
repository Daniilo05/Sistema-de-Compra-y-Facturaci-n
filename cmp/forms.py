from django import forms
from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    email =  forms.CharField(max_length=254)
    class Meta:
        model = Proveedor
        exclude = ['um', 'fm', 'uc', 'fc']
        widgets = {'descripcion': forms.TextInput()}
        
        def __init__(self, *arg, **kwargs):
            super().__Init__(*arg, **kwargs)
            for field in item(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                })