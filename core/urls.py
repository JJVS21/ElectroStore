# core/urls.py
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.Qsomos, name='quienes_somos'),
    path('faq/', views.faq, name='faq'),
]
