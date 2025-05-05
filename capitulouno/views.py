from django.shortcuts import render
from .methods import biseccion, regla_falsa, punto_fijo
from .graph import graficar_funcion

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

        grafico = graficar_funcion(funcion, float(xi), float(xs), resultado) if resultado else None

        context = {
            'tabla': tabla,
            'resultado': resultado,
            'mensaje': mensaje,
            'funcion': funcion,
            'xi': xi,
            'xs': xs,
            'tol': tol,
            'niter': niter,
            'grafico': grafico,
        }

    return render(request, 'biseccion.html', context)


def regla_falsa_view(request):
    context = {}
    if request.method == 'POST':
        funcion = request.POST.get('funcion')
        xi = float(request.POST.get('xi'))
        xs = float(request.POST.get('xs'))
        tol = float(request.POST.get('tol'))
        niter = int(request.POST.get('niter'))

        tabla, resultado, mensaje = regla_falsa(funcion, xi, xs, tol, niter)

        grafico = graficar_funcion(funcion, float(xi), float(xs), resultado) if resultado else None

        context = {
            'tabla': tabla,
            'resultado': resultado,
            'mensaje': mensaje,
            'funcion': funcion,
            'xi': xi,
            'xs': xs,
            'tol': tol,
            'niter': niter,
            'grafico': grafico,
        }

    return render(request, 'reglafalsa.html', context)

def punto_fijo_view(request):
    context = {}
    if request.method == 'POST':
        f_str = request.POST['f']
        g_str = request.POST['g']
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        niter = int(request.POST.get('niter'))

        resultado, tabla, mensaje = punto_fijo(x0, tol, niter, f_str, g_str)
        grafico = graficar_funcion(f_str, x0 - 2, resultado + 5, resultado)

        context = {
            'funcion': f_str,
            'g': g_str,
            'x0': x0,
            'tol': tol,
            'niter': niter,
            'resultado': resultado,
            'tabla': tabla,
            'mensaje': mensaje,
            'grafico': grafico,
        }

    return render(request, 'puntofijo.html', context)
