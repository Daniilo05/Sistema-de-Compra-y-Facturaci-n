from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

# Create your views here.

class SinPermisos(PermissionRequiredMixin):
    raise_exception = False
    redirect_field_name = "redirect_to"
    
    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user== AnonymousUser():
            self.login_url="bases:sin_permisos"
        return HttpResponseRedirect(reverse_lazy(self.login_url))
        
        
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

class HomeSinPermisos(generic.TemplateView):
    template_name = 'bases/sin_permisos.html'