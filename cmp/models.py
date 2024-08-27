from django.db import models
from bases.models import ClaseModelo

class Proveedor(ClaseModelo):
    descripcion =  models.CharField(
        max_length=100,
        unique=True,
    )
    direccion = models.CharField(
        max_length=250,
        null=True, blank=True,
    )
    telefono = models.CharField(
        max_length=10,
        null=True, blank=True,
    )
    email = models.CharField(
        max_length=250,
        null=True, blank=True,
    )
    
    def __str__(self):
        self.descripcion = self.direccion.upper()
        super(Proveedor,self).save()
        
    class Meta:
        verbose_name_plural = "Proveedores"