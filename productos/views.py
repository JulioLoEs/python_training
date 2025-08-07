from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render

from .forms import ProductoForm
from .models import Producto
# Create your views here.


def index(request):

    productos = Producto.objects.all()
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )

    # __gt: greater than
    # productos = Producto.objects.filter(puntaje__gt=3)
    # productos = Producto.objects.get(pk=1)


def detalle(request, producto_id):

    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle.html', context={'producto': producto})


def formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Método save lo guarda en la base de datos
            form.save()
            return HttpResponseRedirect('/productos')
    else:
        form = ProductoForm()

    return render(
        request,
        'producto_form.html',
        {'form': form}
    )
