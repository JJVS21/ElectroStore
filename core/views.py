from django.shortcuts import render

def home(request):
    return render(request, "core/home.html")

def Qsomos(request):
    return render(request, "core/quienes_somos.html")

def faq(request):
    return render(request, "core/faq.html")