from django.urls import path
from .views import CategoriaView, CategoriaNew, CategoriaEdit,CategoriaDelete,SubCategoriaView, SubCategoriaNew,SubCategoriaEdit,SubCategoriaDelete, MarcaView, MarcaNew, MarcaEdit, marca_inactivar, UmView, UmNew, UmEdit, um_inactivar

urlpatterns = [
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>',CategoriaDelete.as_view(), name='categoria_delete'),
    
    path('subcategorias/',SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new',SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>',SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>',SubCategoriaDelete.as_view(), name='subcategoria_delete'),
    
    
    path('marcas/',MarcaView.as_view(), name='marca_list'),
    path('marcas/new',MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>',marca_inactivar, name = 'marca_inactivar'),
    
    
    path('um/', UmView.as_view(), name='um_list'),
    path('um/new', UmNew.as_view(), name="um_new"),
    path('um/edit/<int:pk>',UmEdit.as_view(), name='um_edit'),
    path('um/inactivar/<int:id>',um_inactivar, name='um_inactivar')
 
]
