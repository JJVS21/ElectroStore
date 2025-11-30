from django.urls import path
from . import views
from .views import enviar_correo_prueba


app_name = 'store'  # Define el namespace aquí

urlpatterns = [
    path('filtrar/', views.filtrar_productos, name='filtrar_productos'),
    path('galeria/', views.product_gallery, name='product_gallery'),
    path('productos/<int:pk>/', views.product_detail, name='product_detail'),
    path("test-mail/", enviar_correo_prueba, name="test_mail"),
]

