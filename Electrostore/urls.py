from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404  # Necesario para definir la página 404
from core import views                   # Importa las vistas personalizadas

urlpatterns = [
    path('contacto/', include('contact.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),        # core maneja la página principal
    path('store/', include('store.urls')), # rutas de la tienda
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path("api/", include("api.urls")),
    path("frontapi/", include("frontendapi.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Página 404 personalizada
handler404 = 'core.views.error_404'
