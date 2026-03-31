from django.db import models
from apps.main.models import Producto
from django.contrib.auth.models import User

# Create your models here.

class Carrito(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrito' )
    fec_creacion = models.DateField(auto_now_add=True)
    fec_actualizacion = models.DateField(auto_now=True)

    def __str__(self):
        return f'El cliente {self.cliente}'
    
    def total_producto(self):
        return sum(item.cantidad for item in self.items.all())
    
    def total(self):
        return sum(item.subtotal() for item in self.items.all() )

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['carrito', 'producto']

    def __str__(self):
        return f'{self.producto} * {self.cantidad}'

    def subtotal(self):
        return self.producto.cantidad * self.cantidad 

