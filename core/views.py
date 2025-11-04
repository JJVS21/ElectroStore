from django.shortcuts import render, redirect

def home(request):
    return render(request, "core/home.html")

def Qsomos(request):
    return render(request, "core/quienes_somos.html")

def faq(request):
    return render(request, "core/faq.html")

def galeria(request):
    return redirect('store:product_gallery')


def error_404(request, exception):
    return render(request, '404.html', status=404)