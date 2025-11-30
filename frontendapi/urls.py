from django.urls import path
from .views import productos_api_view, crear_producto_view

urlpatterns = [
    path("productos/", productos_api_view, name="productos_api_view"),
    path("productos/crear/", crear_producto_view, name="crear_producto"),
]
