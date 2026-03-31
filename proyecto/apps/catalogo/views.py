from django.shortcuts import render
from apps.main.models import Producto

# Create your views here.

def catalogo(request):
    catalogo_prod = Producto.objects.all()
    return render(request, 'main/catalogo.html', context={'catalogo_prod':catalogo_prod})