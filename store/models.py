from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('cpu', 'Procesadores'),
        ('ram', 'Memorias RAM'),
        ('gpu', 'Tarjetas Gráficas'),
        ('ssd', 'Almacenamiento SSD'),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(
        max_length=10, 
        choices=CATEGORY_CHOICES,
        default='cpu'
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name