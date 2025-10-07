from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product

def product_gallery(request):
    """
    Muestra todos los productos paginados de 8 en 8.
    """
    # Obtener todos los productos ordenados por fecha de creación
    all_products = Product.objects.all().order_by('-created')
    
    # Paginador: 8 productos por página
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page', 1)
    products = paginator.get_page(page_number)
    
    context = {
        'products': products,
    }
    return render(request, 'store/product_gallery.html', context)


def product_detail(request, pk):
    """
    Muestra el detalle de un producto específico.
    """
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)