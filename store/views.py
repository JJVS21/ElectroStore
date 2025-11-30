# store/views.py
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.core.mail import send_mail

def product_gallery(request):
    page_number = request.GET.get('page', '1')
    categories = ['cpu', 'ram', 'gpu', 'ssd']
    category_names = {
        'cpu': 'Procesadores',
        'ram': 'Memorias RAM',
        'gpu': 'Tarjetas Gráficas',
        'ssd': 'Almacenamiento SSD'
    }

    try:
        page_number = int(page_number)
        if page_number < 1 or page_number > len(categories):
            page_number = 1
        category_key = categories[page_number - 1]
    except (IndexError, ValueError):
        page_number = 1
        category_key = categories[0]

    # CORRECCIÓN: Usar el nombre completo de la categoría del diccionario
    full_category_name = category_names.get(category_key, category_key)
    productos = Producto.objects.filter(categoria__nombre=full_category_name).order_by('-id')

    context = {
        'products': productos,
        'category_name': full_category_name,
        'category_key': category_key,
        'page_number': page_number,
        'total_pages': len(categories),
    }
    return render(request, 'store/product_gallery.html', context)


def product_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'store/product_detail.html', {'product': producto})


def filtrar_productos(request):
    """
    Vista que aplica al menos dos filtros: categoria y precio_max
    Ejemplo: /store/filtrar/?categoria=Procesadores&precio_max=500000
    """
    categoria = request.GET.get('categoria')
    precio_max = request.GET.get('precio_max')

    productos = Producto.objects.all()

    if categoria:
        productos = productos.filter(categoria__nombre__icontains=categoria)

    if precio_max:
        try:
            precio_max_val = float(precio_max)
            productos = productos.filter(precio__lte=precio_max_val)
        except ValueError:
            pass

    context = {
        'productos': productos,
        'categoria': categoria,
        'precio_max': precio_max,
    }
    return render(request, 'store/filtrar_producto.html', context)


def enviar_correo_prueba(request):
    send_mail(
        subject='Probando Mailtrap',
        message='Este es un correo de prueba desde el proyecto.',
        from_email='noreply@proyecto.com',
        recipient_list=['test@example.com'],
    )
    return HttpResponse("Correo enviado (revisar Mailtrap)")
