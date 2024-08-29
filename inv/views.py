from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Categoria,SubCategoria, Marca, Um, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UmForm, ProductoForm

class BasesCreateNew(LoginRequiredMixin, generic.CreateView):
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class BasesUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class BasesDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = "bases:login"
    
    def form_valid(self, form):
       return reverse_lazy(self.success_url_name)
   

def inactivar_modelo(request,modelo, id, template_name, redirect_url):
    obj = modelo.objects.filter(pk=id).first()
    if not obj:
        return redirect(redirect_url)
    if request.method=="POST":
        obj.estado = False
        obj.save()
        return redirect(redirect_url)
    return render(request, template_name, {"obj":obj})
   
class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"

class CategoriaNew(BasesCreateNew):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"

class CategoriaEdit(BasesUpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    login_url = "bases:login"
class CategoriaDelete(BasesDeleteView):
    model = Categoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")
    
    
class SubCategoriaView(LoginRequiredMixin, generic.ListView):
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
    
class SubCategoriaNew(BasesCreateNew):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"
class SubCategoriaEdit(BasesUpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    login_url = "bases:login"
class SubCategoriaDelete(BasesDeleteView): 
    model = SubCategoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    
class MarcaView(LoginRequiredMixin, generic.ListView):
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class MarcaNew(BasesCreateNew):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class MarcaEdit(BasesUpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
def marca_inactivar(request, id):
    return inactivar_modelo(request, Marca, id, "inv/categoria_delete.html", "inv:marca_list")


class UmView(LoginRequiredMixin, generic.ListView):
    model = Um
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
    
class UmNew(BasesCreateNew):
    model = Um
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class = UmForm
    success_url = reverse_lazy("inv:um_list")
    login_url = "bases:login"

class UmEdit(BasesUpdateView):
    model = Um
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class = UmForm
    success_url = reverse_lazy("inv:um_list")
    login_url = "bases:login"

def um_inactivar(request, id):
    return inactivar_modelo(request, Um, id, "inv/um_delete.html", "inv:um_list")
        
    
    return render(request,template_name,contexto)

class ProductoView(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"
    login_url = "bases:login"    
    
class ProductoNew(BasesCreateNew):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"
    
class ProductoEdit(BasesUpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    login_url = "bases:login"
    
def producto_inactivar(request, id):
    return inactivar_modelo(request, Producto, id, "inv/categoria_delete.html", "inv:producto_list")
        
