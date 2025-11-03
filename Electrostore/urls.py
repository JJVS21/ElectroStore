from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.conf.urls import handler404  # ← agregado
from django.shortcuts import render       # ← agregado

urlpatterns = [
    path('contacto/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('quienes-somos/', views.Qsomos, name="quienes_somos"),
    path('faq/', views.faq, name="faq"),
    path('', include('store.urls')),  # Incluye todas las rutas de store
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 🚫 Manejo personalizado del error 404
def error_404_view(request, exception):
    return render(request, '404.html', status=404)

handler404 = error_404_view
