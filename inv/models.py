from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de Categoria',
        unique=True,
    )
    
    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = 'Categorias'
        
    