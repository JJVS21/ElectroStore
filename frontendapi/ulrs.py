from django.urls import path
from .views import productos_api_view

urlpatterns = [
    path("productos/", productos_api_view, name="productos_api_view"),
]
