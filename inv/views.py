from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .models import Categoria,SubCategoria, Marca, Um, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UmForm, ProductoForm

class BasesCreateNew(SuccessMessageMixin, LoginRequiredMixin, generic.CreateView):
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class BasesUpdateView(SuccessMessageMixin, LoginRequiredMixin, generic.UpdateView):
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class BasesDeleteView(LoginRequiredMixin, generic.DeleteView):
    login_url = "bases:login"
    success_url = None
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message)
        return response

def inactivar_modelo(request,modelo, id, template_name, redirect_url):
    obj = modelo.objects.filter(pk=id).first()
    if not obj:
        return redirect(redirect_url)
    if request.method=="POST":
        obj.estado = False
        obj.save()
        messages.success(request, f'{modelo.__name__} inactivado Correctamente')
        return redirect(redirect_url)
    return render(request, template_name, {"obj":obj})
   
class CategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    login_url = "base:login"
    

class CategoriaNew(BasesCreateNew):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Creada Correctamente"

class CategoriaEdit(BasesUpdateView):
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Actualizada Correctamente"
class CategoriaDelete(BasesDeleteView):
    model = Categoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Eliminada Correctamente"
    
    
class SubCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    permission_required = "inv.view_subcategoria"
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
    success_message = "SubCategoria Creada Correctamente"
class SubCategoriaEdit(BasesUpdateView):
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "SubCategoria Actualizada  Correctamente"

class SubCategoriaDelete(BasesDeleteView): 
    model = SubCategoria
    template_name = "inv/categoria_delete.html"
    context_object_name = "obj"
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "SubCategoria Eliminada Correctamente"
    
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
    success_message = "Marca Creada Correctamente"
class MarcaEdit(BasesUpdateView):
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")
    success_message = "Marca Actualizada Correctamente"
    
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
    success_message = "Unidad de Medida Creada Correctamente"

class UmEdit(BasesUpdateView):
    model = Um
    template_name = "inv/um_form.html"
    context_object_name = "obj"
    form_class = UmForm
    success_url = reverse_lazy("inv:um_list")
    success_message = "Unidad de Medida Actualizada Correctamente"

def um_inactivar(request, id):
    return inactivar_modelo(request, Um, id, "inv/categoria_delete.html", "inv:um_list")
        
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
    success_message = "Producto Creada Correctamente"

    
class ProductoEdit(BasesUpdateView):
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")
    success_message = "Producto Actualizada Correctamente"
    
def producto_inactivar(request, id):
    return inactivar_modelo(request, Producto, id, "inv/categoria_delete.html", "inv:producto_list")
        
