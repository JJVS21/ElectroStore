from django.shortcuts import render

import requests
from django.shortcuts import render

def productos_api_view(request):
    url = "http://127.0.0.1:8000/api/productos/"
    respuesta = requests.get(url)
    productos = respuesta.json()

    return render(request, "frontendapi/lista_productos.html", {"productos": productos})

