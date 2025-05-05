from django.shortcuts import render
from .methods import biseccion, regla_falsa, punto_fijo, newton_raphson, secante, raices_multiples, calcular_funcion_g_optima
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

def newton_view(request):
    context = {}
    if request.method == 'POST':
        f_str = request.POST.get('f')
        x0 = float(request.POST.get('x0'))
        tol = float(request.POST.get('tol'))
        niter = int(request.POST.get('niter'))

        resultado, tabla, mensaje = newton_raphson(x0, tol, niter, f_str)
        grafico = graficar_funcion(f_str, x0 - 2, resultado + 5, resultado)

        context = {
            'funcion': f_str,
            'x0': x0,
            'tol': tol,
            'niter': niter,
            'resultado': resultado,
            'tabla': tabla,
            'mensaje': mensaje,
            'grafico': grafico,
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

        resultado, tabla, mensaje = secante(x0, x1, tol, niter, f_str)
        grafico = graficar_funcion(f_str, x0 - 5, x1 + 5, resultado)

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
        }

    return render(request, 'secante.html', context)

def raices_multiples_view(request):
    context = {}
    if request.method == 'POST':
        f_str = request.POST['f']
        x0 = float(request.POST['x0'])
        tol = float(request.POST['tol'])
        niter = int(request.POST['niter'])
        
        # Ejecutar el método de Raíces Múltiples
        resultado, tabla, mensaje = raices_multiples(x0, tol, niter, f_str)
        grafico = graficar_funcion(f_str, x0 - 5, x0 + 5, resultado)

        # Ejecutar los demás métodos
        resultados_comparativos = []
        
        # Bisección - necesita un intervalo, usaremos x0-2 y x0+2
        xi = x0 - 2
        xs = x0 + 2
        tabla_biseccion, resultado_biseccion, mensaje_biseccion = biseccion(f_str, xi, xs, tol, niter)
        if resultado_biseccion is not None:
            n_biseccion = len(tabla_biseccion) - 1
            error_biseccion = tabla_biseccion[-1][3] if n_biseccion > 0 and tabla_biseccion[-1][3] is not None else "N/A"
            resultados_comparativos.append({
                'metodo': 'Bisección',
                'xs': resultado_biseccion,
                'n': n_biseccion,
                'error': error_biseccion
            })

        else:
            # Añadir mensaje de error
            resultados_comparativos.append({
                'metodo': 'Bisección',
                'xs': "N/A",
                'n': "N/A",
                'error': "N/A",
                'info': mensaje_biseccion  # "Intervalo inadecuado"
            })
        
        # Regla Falsa - necesita un intervalo, usaremos x0-2 y x0+2
        tabla_regla_falsa, resultado_regla_falsa, mensaje_regla_falsa = regla_falsa(f_str, xi, xs, tol, niter)
        if resultado_regla_falsa is not None:
            n_regla_falsa = len(tabla_regla_falsa) - 1
            error_regla_falsa = tabla_regla_falsa[-1][3] if n_regla_falsa > 0 and tabla_regla_falsa[-1][3] is not None else "N/A"
            resultados_comparativos.append({
                'metodo': 'Regla Falsa',
                'xs': resultado_regla_falsa,
                'n': n_regla_falsa,
                'error': error_regla_falsa
            })

        else:
            # Añadir mensaje de error
            resultados_comparativos.append({
                'metodo': 'Regla Falsa',
                'xs': "N/A",
                'n': "N/A",
                'error': "N/A",
                'info': mensaje_regla_falsa
            })
        
        # Punto Fijo - calcular automáticamente una buena función g(x)
        g_str, convergencia_info = calcular_funcion_g_optima(f_str, x0)
        resultado_punto_fijo, tabla_punto_fijo, mensaje_punto_fijo = punto_fijo(x0, tol, niter, f_str, g_str)
        if resultado_punto_fijo is not None:
            n_punto_fijo = len(tabla_punto_fijo) - 1
            error_punto_fijo = tabla_punto_fijo[-1][3] if n_punto_fijo > 0 and tabla_punto_fijo[-1][3] is not None else "N/A"
            resultados_comparativos.append({
                'metodo': 'Punto Fijo',
                'xs': resultado_punto_fijo,
                'n': n_punto_fijo,
                'error': error_punto_fijo,
                'g_str': g_str,
                'convergencia_info': convergencia_info
            })

        else:
            # Añadir mensaje de error
            resultados_comparativos.append({
                'metodo': 'Punto Fijo',
                'xs': "N/A",
                'n': "N/A",
                'error': "N/A",
                'info': mensaje_punto_fijo
            })
        
        # Newton-Raphson
        resultado_newton, tabla_newton, mensaje_newton = newton_raphson(x0, tol, niter, f_str)
        if resultado_newton is not None:
            n_newton = len(tabla_newton) - 1
            error_newton = tabla_newton[-1][3] if n_newton > 0 and tabla_newton[-1][3] is not None else "N/A"
            resultados_comparativos.append({
                'metodo': 'Newton',
                'xs': resultado_newton,
                'n': n_newton,
                'error': error_newton
            })

        else:
            # Añadir mensaje de error
            resultados_comparativos.append({
                'metodo': 'Newton',
                'xs': "N/A",
                'n': "N/A",
                'error': "N/A",
                'info': mensaje_newton
            })
        
        # Secante - necesita dos puntos iniciales, usaremos x0 y x0+0.1
        x1 = x0 + 0.1
        resultado_secante, tabla_secante, mensaje_secante = secante(x0, x1, tol, niter, f_str)
        if resultado_secante is not None:
            n_secante = len(tabla_secante) - 1
            error_secante = tabla_secante[-1][3] if n_secante > 0 and tabla_secante[-1][3] is not None else "N/A"
            resultados_comparativos.append({
                'metodo': 'Secante',
                'xs': resultado_secante,
                'n': n_secante,
                'error': error_secante
            })

        else:
            # Añadir mensaje de error
            resultados_comparativos.append({
                'metodo': 'Secante',
                'xs': "N/A",
                'n': "N/A",
                'error': "N/A",
                'info': mensaje_secante
            })
        
        # Raíces Múltiples (ya calculado)
        n_rm = len(tabla) - 1
        error_rm = tabla[-1][3] if n_rm > 0 and tabla[-1][3] is not None else "N/A"
        resultados_comparativos.append({
            'metodo': 'Raíces Múltiples',
            'xs': resultado,
            'n': n_rm,
            'error': error_rm
        })

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