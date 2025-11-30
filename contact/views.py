from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

def contacto(request):
    enviado = False

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            email = form.cleaned_data["email"]
            asunto = form.cleaned_data["asunto"]
            mensaje = form.cleaned_data["mensaje"]

            texto = f"""
Nombre: {nombre}
Correo: {email}

Mensaje:
{mensaje}
"""

            send_mail(
                subject=asunto,
                message=texto,
                from_email=settings.DEFAULT_FROM_EMAIL,  # correcto para Mailtrap
                recipient_list=["TU-INBOX@inbox.mailtrap.io"],  # reemplazar con tu correo real
                fail_silently=False
            )

            enviado = True
    else:
        form = ContactForm()

    return render(request, "contact/contacto.html", {"form": form, "enviado": enviado})

