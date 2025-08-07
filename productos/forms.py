from . import models
# ModelForm: importa formularios con base en los modelos
from django.forms import ModelForm


class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']
