from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from .models import ProductoExtra


@method_decorator(csrf_exempt, name='dispatch')
def productos_api(request):
    
    # GET → devolver todos los productos en JSON
    if request.method == "GET":
        productos = list(ProductoExtra.objects.values())
        return JsonResponse(productos, safe=False)

    # POST → crear producto desde JSON
    if request.method == "POST":
        data = json.loads(request.body)

        nuevo = ProductoExtra.objects.create(
            nombre=data.get("nombre"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock")
        )

        return JsonResponse(
            {"mensaje": "Producto creado", "id": nuevo.id},
            status=201
        )

    return JsonResponse({"error": "Método no permitido"}, status=405)

