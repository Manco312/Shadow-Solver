import numpy as np
from django.shortcuts import render
from .methods import jacobi, gauss_seidel, sor

# Create your views here.

def optionsch2(request):
    return render(request, 'optionsch2.html')

def jacobi_view(request):
    context = {
        'matrix_size': 2, # Tamaño de la matriz por defecto
    }
    if request.method == 'POST':
        try:
            size = int(request.POST.get('matrix_size', 2))

            # Leer matriz A
            A = []
            for i in range(size):
                fila = []
                for j in range(size):
                    val = float(request.POST.get(f'a_{i}_{j}'))
                    fila.append(val)
                A.append(fila)

            # Leer vector b
            b = [float(request.POST.get(f'b_{i}')) for i in range(size)]

            # Leer vector x0
            x0 = [float(request.POST.get(f'x0_{i}')) for i in range(size)]

            tol = float(request.POST['tol'])
            niter = int(request.POST['niter'])

            usar_cifras = request.POST.get('usar_cifras') == 'on'

            tabla, mensaje = jacobi(x0, A, b, tol, niter, usar_cifras)

            context = {
                'tabla': tabla,
                'mensaje': mensaje,
                'matrix_size': size,
                'A': A,
                'b': b,
                'x0': x0,
                'tol': tol,
                'niter': niter
            }

        except Exception as e:
            mensaje = f"Error: {str(e)}"

    return render(request, 'jacobi.html', context)


def gauss_seidel_view(request):
    context = {
        'matrix_size': 2,
    }
    if request.method == 'POST':
        try:
            size = int(request.POST.get('matrix_size', 2))

            A = []
            for i in range(size):
                fila = []
                for j in range(size):
                    val = float(request.POST.get(f'a_{i}_{j}'))
                    fila.append(val)
                A.append(fila)

            b = [float(request.POST.get(f'b_{i}')) for i in range(size)]
            x0 = [float(request.POST.get(f'x0_{i}')) for i in range(size)]

            tol = float(request.POST['tol'])
            niter = int(request.POST['niter'])
            usar_cifras = request.POST.get('usar_cifras') == 'on'

            tabla, mensaje = gauss_seidel(x0, A, b, tol, niter, usar_cifras)

            context = {
                'tabla': tabla,
                'mensaje': mensaje,
                'matrix_size': size,
                'A': A,
                'b': b,
                'x0': x0,
                'tol': tol,
                'niter': niter,
                'usar_cifras': usar_cifras
            }
        except Exception as e:
            context['mensaje'] = f"Error: {str(e)}"

    return render(request, 'gauss_seidel.html', context)


def sor_view(request):
    context = {
        'matrix_size': 2,
    }

    if request.method == 'POST':
        try:
            size = int(request.POST.get('matrix_size', 2))

            A = []
            for i in range(size):
                fila = []
                for j in range(size):
                    val = float(request.POST.get(f'a_{i}_{j}'))
                    fila.append(val)
                A.append(fila)

            b = [float(request.POST.get(f'b_{i}')) for i in range(size)]
            x0 = [float(request.POST.get(f'x0_{i}')) for i in range(size)]

            tol = float(request.POST['tol'])
            niter = int(request.POST['niter'])
            w = float(request.POST['w'])
            usar_cifras = request.POST.get('usar_cifras') == 'on'

            tabla, mensaje = sor(x0, A, b, tol, niter, w, usar_cifras)

            context.update({
                'tabla': tabla,
                'mensaje': mensaje,
                'matrix_size': size,
                'A': A,
                'b': b,
                'x0': x0,
                'tol': tol,
                'niter': niter,
                'w': w,
                'usar_cifras': usar_cifras
            })

        except Exception as e:
            context['mensaje'] = f"Error: {str(e)}"

    return render(request, 'sor.html', context)
