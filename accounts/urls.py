from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registro/vendedor/', views.register_seller, name='register_seller'),
    path('registro/manager/', views.register_manager, name='register_manager'),
]
