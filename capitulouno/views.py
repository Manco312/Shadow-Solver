from django.shortcuts import render
from .methods import biseccion

# Create your views here.

def optionsch1(request):
    return render(request, 'optionsch1.html')

def biseccion_view(request):
    context = {}
    if request.method == 'POST':
        funcion = request.POST.get('funcion')
        xi = float(request.POST.get('xi'))
        xs = float(request.POST.get('xs'))
        tol = float(request.POST.get('tol'))
        niter = int(request.POST.get('niter'))

        tabla, resultado, mensaje = biseccion(funcion, xi, xs, tol, niter)

        context = {
            'tabla': tabla,
            'resultado': resultado,
            'mensaje': mensaje,
            'funcion': funcion,
            'xi': xi,
            'xs': xs,
            'tol': tol,
            'niter': niter
        }

    return render(request, 'biseccion.html', context)
