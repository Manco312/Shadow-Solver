from sympy import symbols, sympify
from sympy.utilities.lambdify import lambdify

def biseccion(f_expr_str, xi, xs, Tol, niter):
    x = symbols('x')
    f_expr = sympify(f_expr_str)
    f = lambdify(x, f_expr, 'math')

    fi = f(xi)
    fs = f(xs)

    resultados = []

    if fi == 0:
        resultados.append((0, xi, fi, 0))
        return resultados, xi, "es raíz exacta"
    elif fs == 0:
        resultados.append((0, xs, fs, 0))
        return resultados, xs, "es raíz exacta"
    elif fi * fs < 0:
        c = 0
        xm = (xi + xs) / 2
        fe = f(xm)
        error = Tol + 1
        resultados.append((c, xm, fe, None))

        while error > Tol and fe != 0 and c < niter:
            if fi * fe < 0:
                xs = xm
                fs = f(xs)
            else:
                xi = xm
                fi = f(xi)
            xa = xm
            xm = (xi + xs) / 2
            fe = f(xm)
            error = abs(xm - xa)
            c += 1
            resultados.append((c, xm, fe, error))

        if fe == 0:
            mensaje = "es raíz exacta"
        elif error < Tol:
            mensaje = f"es una aproximación con tolerancia {Tol}"
        else:
            mensaje = f"falló en {niter} iteraciones"
        return resultados, xm, mensaje
    else:
        return [], None, "Intervalo inadecuado"
