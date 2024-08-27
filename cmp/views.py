from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import json
from .models import Proveedor
from .forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = reverse_lazy('bases:login')
    
class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = reverse_lazy('bases:login')
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
    model =  Proveedor
    template_name = 'cmp/proveedor_form.html'
    form = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = reverse_lazy('bases:login')
    
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)
    
def proveedor_inactivar(request,id):
    template_name ='cmp/inactivar_prv.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()
    
    if not prv:
        return HttpResponse('Proveedor no existe' + str(id))
    if request.method == 'GET':
        contexto={'obj':prv}
        
    if request.method=='POST':
        prv.estado = False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivo')
        
    return render(request,template_name,contexto)