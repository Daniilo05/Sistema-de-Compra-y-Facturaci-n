from django.db import models
from bases.models import ClaseModelo

# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text=
    )