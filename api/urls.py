from django.urls import path
from .views import productos_api

urlpatterns = [
    path("productos/", productos_api, name="api_productos"),
]
