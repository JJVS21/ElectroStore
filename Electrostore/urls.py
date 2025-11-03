from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.conf.urls import handler404  # ← agregado
from django.shortcuts import render       # ← agregado

# Electrostore/urls.py (fragmento)
urlpatterns = [
    path('contacto/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),       # ahora core gestiona la raíz
    path('store/', include('store.urls')), # store bajo /store/
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Electrostore/urls.py (reemplaza la función existente)
def error_404_view(request, exception):
    return render(request, 'core/404.html', status=404)
handler404 = error_404_view


