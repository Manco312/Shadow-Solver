from django.shortcuts import render
from .methods import biseccion, regla_falsa, punto_fijo, newton_raphson, secante, raices_multiples, ejecutar_todos
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

        usar_cifras = request.POST.get('usar_cifras') == 'on'

        tabla, resultado, mensaje = biseccion(funcion, xi, xs, tol, niter, usar_cifras)
        grafico = graficar_funcion(funcion, float(xi), float(xs), resultado) if resultado else None

        comparar = request.POST.get('comparar') == 'on'

        if comparar:
            # Ejecutar todos los métodos
            resultados_comparativos = ejecutar_todos(f_str=funcion, g_str=None, xi=xi, xs=xs, tol=tol, niter=niter, x1=None, cs=usar_cifras)
        else:
            resultados_comparativos = None

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
            'resultados_comparativos': resultados_comparativos
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

        usar_cifras = request.POST.get('usar_cifras') == 'on'

        tabla, resultado, mensaje = regla_falsa(funcion, xi, xs, tol, niter, usar_cifras)
        grafico = graficar_funcion(funcion, float(xi), float(xs), resultado) if resultado else None

        comparar = request.POST.get('comparar') == 'on'

        if comparar:
            # Ejecutar todos los métodos
            resultados_comparativos = ejecutar_todos(f_str=funcion, g_str=None, xi=xi, xs=xs, tol=tol, niter=niter, x1=None, cs=usar_cifras)
        else:
            resultados_comparativos = None

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
            'resultados_comparativos': resultados_comparativos
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

        usar_cifras = request.POST.get('usar_cifras') == 'on'

        resultado, tabla, mensaje = punto_fijo(x0, tol, niter, f_str, g_str, usar_cifras)
        grafico = graficar_funcion(f_str, x0 - 2, resultado + 5, resultado)

        comparar = request.POST.get('comparar') == 'on'

        if comparar:
            # Ejecutar todos los métodos
            resultados_comparativos = ejecutar_todos(f_str=f_str, g_str=g_str, xi=x0, xs=None, tol=tol, niter=niter, x1=None, cs=usar_cifras)
        else:
            resultados_comparativos = None

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
            'resultados_comparativos': resultados_comparativos
        }

    return render(request, 'puntofijo.html', context)

def newton_view(request):
    context = {}
    if request.method == 'POST':
        f_str = request.POST.get('f')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        niter = int(request.POST.get('niter'))

        usar_cifras = request.POST.get('usar_cifras') == 'on'

        resultado, tabla, mensaje = newton_raphson(x0, tol, niter, f_str, usar_cifras)
        grafico = graficar_funcion(f_str, x0 - 2, resultado + 5, resultado)

        comparar = request.POST.get('comparar') == 'on'

        if comparar:
            # Ejecutar todos los métodos
            resultados_comparativos = ejecutar_todos(f_str=f_str, g_str=None, xi=x0, xs=None, tol=tol, niter=niter, x1=None, cs=usar_cifras)
        else:
            resultados_comparativos = None

        context = {
            'funcion': f_str,
            'x0': x0,
            'tol': tol,
            'niter': niter,
            'resultado': resultado,
            'tabla': tabla,
            'mensaje': mensaje,
            'grafico': grafico,
            'resultados_comparativos': resultados_comparativos
        }

    return render(request, 'newton.html', context)

def secante_view(request):
    context = {}
    if request.method == 'POST':
        f_str = request.POST['f']
        x0 = float(request.POST['x0'])
        x1 = float(request.POST['x1'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        usar_cifras = request.POST.get('usar_cifras') == 'on'

        resultado, tabla, mensaje = secante(x0, x1, tol, niter, f_str, usar_cifras)
        grafico = graficar_funcion(f_str, x0 - 5, x1 + 5, resultado)

        comparar = request.POST.get('comparar') == 'on'

        if comparar:
            # Ejecutar todos los métodos
            resultados_comparativos = ejecutar_todos(f_str=f_str, g_str=None, xi=x0, xs=None, tol=tol, niter=niter, x1=x1, cs=usar_cifras)
        else:
            resultados_comparativos = None

        context = {
            'funcion': f_str,
            'x0': x0,
            'x1': x1,
            'tol': tol,
            'niter': niter,
            'resultado': resultado,
            'tabla': tabla,
            'mensaje': mensaje,
            'grafico': grafico,
            'resultados_comparativos': resultados_comparativos
        }

    return render(request, 'secante.html', context)

def raices_multiples_view(request):
    context = {}
    if request.method == 'POST':
        f_str = request.POST['f']
        x0 = float(request.POST['x0'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])

        usar_cifras = request.POST.get('usar_cifras') == 'on'
        
        # Ejecutar el método de Raíces Múltiples
        resultado, tabla, mensaje = raices_multiples(x0, tol, niter, f_str, usar_cifras)
        grafico = graficar_funcion(f_str, x0 - 5, x0 + 5, resultado)

        comparar = request.POST.get('comparar') == 'on'

        if comparar:
            # Ejecutar todos los métodos
            resultados_comparativos = ejecutar_todos(f_str=f_str, g_str=None, xi=x0, xs=None, tol=tol, niter=niter, x1=None, cs=usar_cifras)
        else:
            resultados_comparativos = None

        context = {
            'f': f_str,
            'x0': x0,
            'tol': tol,
            'niter': niter,
            'resultado': resultado,
            'tabla': tabla,
            'mensaje': mensaje,
            'grafico': grafico,
            'resultados_comparativos': resultados_comparativos
        }

    return render(request, 'raicesmultiples.html', context)