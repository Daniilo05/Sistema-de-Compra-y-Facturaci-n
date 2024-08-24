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
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'
        
        
class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de Categoria'
    )
    
    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()
    
    class Meta:
        verbose_name_plural = ' sub Categorias'
        unique_together = ('categoria', 'descripcion')
        
        
class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de Marca',
        unique=True,
    )
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()

    class Meta:
        verbose_name_plural = 'Marca'


class Um(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de Unidad Medida',
        unique=True,
    )
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Um, self).save()
        
    class Meta:
        verbose_name_plural = 'Unidad de Medida'
    
    
class Producto(ClaseModelo):
    codigo = models.CharField(
        max_length=20,
        unique=True,
    )
    codigo_barra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio =  models.FloatField(default=0)
    existencias = models.IntegerField(default=0)
    ultima_compra =  models.DateField(null=True, blank=True)
    
    marca =  models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(Um, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)     
    
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion =  self.descripcion.upper()
        super(Producto, self).save()
        
        
    class Meta:
        verbose_name_plural = 'Productos'
        unique_together = ('codigo','codigo_barra')