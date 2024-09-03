from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Proveedor
from .forms import ProveedorForm

class BasesCreateView(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView):
    login_url = 'base:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class BasesEditView(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    login_url = 'base:login'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = ('bases:login')
    
class ProveedorNew(BasesCreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    success_message ="Proveedor Creado Correctamente"
        
class ProveedorEdit(BasesEditView):
    model =  Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    success_message ="Proveedor Actualizado Correctamente"
      
      
def proveedor_inactivar(request,id):
    proveedor = get_object_or_404(Proveedor,pk=id)
    
    if request.method=='POST':
        proveedor.estado = False
        proveedor.save()
        messages.success(request, "Proveedor inactivado exitosamente.")
        return redirect('cmp:proveedor_list')
        
    return render(request, 'cmp/inactivar_prv.html', {'obj': proveedor})