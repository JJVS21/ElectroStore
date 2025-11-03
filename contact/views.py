from django.shortcuts import render
from .forms import ContactForm

def contacto(request):
    form = ContactForm()
    return render(request, 'contact/contacto.html', {'form': form})
