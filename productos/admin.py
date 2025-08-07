from django.contrib import admin
from .models import Categoria, Producto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class DeporteAdmin(admin.ModelAdmin):
    # Para esconder campos del formulario se puede aplicar exclude. Recibe una tupla
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'puntaje',
                    'categoria', 'creado_en')

    # Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, DeporteAdmin)
