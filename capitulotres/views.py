import numpy as np
from django.shortcuts import render
from django.contrib import messages
from .methods import vandermonde_interpolation
from .graph import graficar_vandermonde

# Create your views here.
def optionsch3(request):
    return render(request, 'optionsch3.html')

def vandermonde_view(request):
    if request.method == 'POST':
        try:
            num_puntos = int(request.POST.get('num_puntos', 0))
            x_vals = []
            y_vals = []
            for i in range(num_puntos):
                x_i = request.POST.get(f'x_{i}')
                y_i = request.POST.get(f'y_{i}')
                if x_i is None or y_i is None or x_i.strip() == '' or y_i.strip() == '':
                    messages.error(request, "Todos los puntos deben estar completos.")
                    return render(request, 'vandermonde.html')
                x_vals.append(float(x_i))
                y_vals.append(float(y_i))

            x = np.array(x_vals)
            y = np.array(y_vals)

            if len(x) != len(y):
                messages.error(request, "Los vectores x e y deben tener la misma cantidad de datos.")
                return render(request, 'vandermonde.html', {'x_vals': x_vals, 'y_vals': y_vals, 'num_puntos': num_puntos})

            if len(x) < 2:
                messages.error(request, "Debes ingresar al menos 2 puntos.")
                return render(request, 'vandermonde.html', {'x_vals': x_vals, 'y_vals': y_vals, 'num_puntos': num_puntos})

            a, poly_str, xpol, p, mensaje_error = vandermonde_interpolation(x, y)
            image_base64 = graficar_vandermonde(x, y, xpol, p)

            return render(request, 'vandermonde.html', {
                'poly_str': poly_str,
                'image_base64': image_base64,
                'mensaje_error': mensaje_error,
                'x_vals': x_vals,
                'y_vals': y_vals,
                'num_puntos': num_puntos
            })

        except ValueError:
            messages.error(request, "Por favor, ingresa solo valores numéricos.")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {str(e)}")

        return render(request, 'vandermonde.html')

    else:
        # GET request: puedes enviar un valor por defecto para num_puntos
        return render(request, 'vandermonde.html', {'num_puntos': 2})


def newton_int_view(request):
    return render(request, 'newton_int.html')

def lagrange(request):
    return render(request, 'lagrange.html')

def spline_view(request):
    return render(request, 'spline.html')
