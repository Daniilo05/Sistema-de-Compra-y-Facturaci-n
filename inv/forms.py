from django import forms
from .models import Categoria, SubCategoria, Marca, Um, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripcion de la categoria','estado': 'Estado'}
        widgets = {'descripcion': forms.TextInput}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter (self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset= Categoria.objects.filter(estado=True)
        .order_by('descripcion')
        
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'descripcion': 'Sub categoria','estado': 'Estado'}
        widgets = {'descripcion': forms.TextInput}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter (self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['categoria'].empty_label = "Seleccione Categoria"
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripcion de la marca','estado': 'Estado'}
        widgets = {'descripcion': forms.TextInput}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter (self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            
            
class UmForm(forms.ModelForm):
    class Meta:
        model = Um
        fields = ['descripcion', 'estado']
        labels = {'descripcion': 'Descripcion de Unidad de medidad', 'estado': 'Estado'}
        widgets = {'descripcion': forms.TextInput}
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter (self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

            
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields =['codigo','codigo_barra','descripcion','estado',
                 'precio','existencias','ultima_compra',
                 'marca','subcategoria','unidad_medida']
        exclude = ['um','fm','uc','fc']
        widgets= {'descripcion': forms.TextInput()}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['ultima_compra'].widget.attrs['readonly'] = True
        self.fields['existencias'].widget.attrs['readonly'] = True