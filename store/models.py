from django.db import models
from django.utils import timezone





class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    image = models.ImageField(upload_to='productos/', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)  # ← Cambiado
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    fecha = models.DateField(auto_now_add=True)
    productos = models.ManyToManyField(Producto)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente}"