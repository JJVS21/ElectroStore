from django.contrib import admin
from .models import Categoria, Producto, Pedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')     # 1️⃣
    search_fields = ('nombre', 'categoria__nombre')               # 2️⃣
    list_filter = ('categoria', 'precio')                         # 3️⃣
    ordering = ('nombre',)                                        # 4️⃣
    list_editable = ('precio', 'stock')                           # 5️⃣

admin.site.register(Categoria)
admin.site.register(Pedido)
