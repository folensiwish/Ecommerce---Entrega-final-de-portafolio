from django.shortcuts import render

from apps.main.models import Producto
# Create your views here.

def carrito(request):
    carrito_prod = Producto.objects.all()
    return render(request, 'carrito/carrito.html', context={
        'carrito_prod':carrito_prod,})
