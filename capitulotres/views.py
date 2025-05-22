from django.shortcuts import render

# Create your views here.
def optionsch3(request):
    return render(request, 'optionsch3.html')

def vandermonde_view(request):
    return render(request, 'vandermonde.html')

def newton_int_view(request):
    return render(request, 'newton_int.html')

def lagrange(request):
    return render(request, 'lagrange.html')

def spline_view(request):
    return render(request, 'spline.html')
