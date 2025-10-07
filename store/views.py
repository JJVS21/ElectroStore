from django.shortcuts import render, get_object_or_404
from .models import Product

def product_gallery(request):
    """
    Muestra los productos agrupados por categoría, una categoría por página.
    """
    page_number = request.GET.get('page', '1')

    categories = ['cpu', 'ram', 'gpu', 'ssd']
    category_names = {
        'cpu': 'Procesadores',
        'ram': 'Memorias RAM',
        'gpu': 'Tarjetas Gráficas',
        'ssd': 'Almacenamiento SSD'
    }

    # Controlar si la página existe
    try:
        page_number = int(page_number)
        if page_number < 1 or page_number > len(categories):
            page_number = 1
        category_key = categories[page_number - 1]
    except (IndexError, ValueError):
        page_number = 1
        category_key = categories[0]

    # Filtrar productos por categoría
    products = Product.objects.filter(category=category_key).order_by('-created')

    context = {
        'products': products,
        'category_name': category_names[category_key],
        'category_key': category_key,
        'page_number': page_number,
        'total_pages': len(categories),
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