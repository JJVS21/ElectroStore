from datetime import datetime

def info_general(request):
    """
    Procesador de contexto que agrega variables globales a todas las plantillas.
    """
    return {
        'año_actual': datetime.now().year,
        'nombre_sitio': 'ElectroStore'
    }

#Este archivo define una función (info_general) que devuelve variables que estarán disponibles en todas las plantillas automáticamente, sin necesidad de pasarlas desde cada vista.