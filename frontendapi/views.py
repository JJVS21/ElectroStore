import requests
from django.shortcuts import render, redirect
from store.models import Categoria


def productos_api_view(request):
    url = "http://127.0.0.1:8000/api/productos/"
    respuesta = requests.get(url)

    print("STATUS:", respuesta.status_code)
    print("RESPUESTA RAW:", respuesta.text)

    productos = respuesta.json()   # ← aquí está explotando
    return render(request, "frontendapi/lista_productos.html", {"productos": productos})



def crear_producto_view(request):

    categorias = Categoria.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        categoria = request.POST.get("categoria")

        data = {
            "nombre": nombre,
            "descripcion": descripcion,
            "precio": precio,
            "stock": stock,
            "categoria": categoria
        }

        respuesta = requests.post(
            "http://127.0.0.1:8000/api/productos/",
            json=data
        )

        if respuesta.status_code == 201:
            return render(request, "frontendapi/crear_exito.html")

    return render(request, "frontendapi/crear_producto.html", {"categorias": categorias})
