from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from store.models import Producto, Categoria


@csrf_exempt
def productos_api(request):

    # GET → Lista todos los productos
    if request.method == "GET":
        productos = list(
            Producto.objects.values(
                "id",
                "nombre",
                "precio",
                "stock",
                "categoria_id",
                "image",
                "created",
                "updated"
            )
        )
        return JsonResponse(productos, safe=False)

    # POST → Crear producto
    if request.method == "POST":
        data = json.loads(request.body)

        categoria_id = data.get("categoria")
        if not Categoria.objects.filter(id=categoria_id).exists():
            return JsonResponse({"error": "Categoría no existe"}, status=400)

        nuevo = Producto.objects.create(
            nombre=data.get("nombre"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            categoria_id=categoria_id
        )

        return JsonResponse(
            {"mensaje": "Producto creado", "id": nuevo.id},
            status=201
        )

    return JsonResponse({"error": "Método no permitido"}, status=405)
