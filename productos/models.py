from django.db import models
from django.utils import timezone

# Create your models here.

# Con models.Model, se está extendiendo de las clases de django


class Categoria(models.Model):
    # charfield: cadena de texto limitada. Recibe como argumento la longitud del string
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # cascade: elimina el producto
    # protect: lanza error
    # restrict: elimina si no existen productos
    # set_null: actualiza a valor nulo
    # set_default: asigna valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
