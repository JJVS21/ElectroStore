from django.shortcuts import render

def home(request):  # Vista backend
    return render(request, "core/home.html")

def Qsomos(request):  # Vista backend
    return render(request, "core/quienes_somos.html")

def faq(request):  # Vista backend
    return render(request, "core/faq.html")

#def galeria(request):  # Vista backend
    return render(request, "core/galeria.html")
