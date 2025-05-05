from sympy import symbols, sympify, Symbol, diff
from sympy.utilities.lambdify import lambdify
import numpy as np

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

def regla_falsa(f_str, xi, xs, tol, niter):
    x = Symbol('x')
    f_expr = sympify(f_str)
    f = lambdify(x, f_expr, 'math')  # 'math' para coherencia con bisección

    fxi = f(xi)
    fxs = f(xs)

    if fxi == 0:
        return [(0, xi, fxi, 0)], xi, "es raíz exacta"
    elif fxs == 0:
        return [(0, xs, fxs, 0)], xs, "es raíz exacta"
    elif fxi * fxs < 0:
        tabla = []
        error = tol + 1
        xm_old = xi
        c = 0
        xm = xs - fxs * (xi - xs) / (fxi - fxs)
        fxm = f(xm)
        tabla.append((c, xm, fxm, None))

        while error > tol and fxm != 0 and c < niter:
            if fxi * fxm < 0:
                xs = xm
                fxs = fxm
            else:
                xi = xm
                fxi = fxm

            xm_old = xm
            xm = xs - fxs * (xi - xs) / (fxi - fxs)
            fxm = f(xm)
            error = abs(xm - xm_old)
            c += 1
            tabla.append((c, xm, fxm, error))

        if fxm == 0:
            mensaje = "es raíz exacta"
        elif error < tol:
            mensaje = f"es una aproximación con tolerancia {tol}"
        else:
            mensaje = f"falló en {niter} iteraciones"
        return tabla, xm, mensaje
    else:
        return [], None, "Intervalo inadecuado"

def punto_fijo(x0, tol, niter, f_str, g_str):
    x = symbols('x')
    f_expr = sympify(f_str)
    g_expr = sympify(g_str)

    f = lambdify(x, f_expr, modules=["numpy"])
    g = lambdify(x, g_expr, modules=["numpy"])

    tabla = []
    c = 0
    xn = x0
    fxn = f(xn)
    error = tol + 1

    tabla.append((c, xn, fxn, None))

    while error > tol and fxn != 0 and c < niter:
        x_next = g(xn)
        fxn = f(x_next)
        error = abs(x_next - xn)  # Error absoluto
        xn = x_next
        c += 1
        tabla.append((c, xn, fxn, error))

    if fxn == 0:
        mensaje = f"{xn} es raíz de f(x)"
    elif error < tol:
        mensaje = f"{xn} es una aproximación de una raíz con tolerancia = {tol}"
    else:
        mensaje = f"Fracasó en {niter} iteraciones"

    return xn, tabla, mensaje

def newton_raphson(x0, tol, niter, f_str):
    x = symbols('x')
    f_expr = sympify(f_str)
    df_expr = diff(f_expr, x)

    f = lambdify(x, f_expr, modules=["numpy"])
    df = lambdify(x, df_expr, modules=["numpy"])

    tabla = []
    c = 0
    xn = x0
    fxn = f(xn)
    dfxn = df(xn)
    error = tol + 1

    tabla.append((c, xn, fxn, None))

    while error > tol and fxn != 0 and dfxn != 0 and c < niter:
        x_next = xn - fxn / dfxn
        fxn = f(x_next)
        dfxn = df(x_next)
        error = abs(x_next - xn)
        xn = x_next
        c += 1
        tabla.append((c, xn, fxn, error))

    # Generar mensaje de resultado
    if fxn == 0:
        mensaje = f"{xn} es raíz de f(x)"
    elif error < tol:
        mensaje = f"{xn} es una aproximación de una raíz con tolerancia = {tol}"
    elif dfxn == 0:
        mensaje = f"{xn} es una posible raíz múltiple (f'(x) = 0)"
    else:
        mensaje = f"Fracasó en {niter} iteraciones"

    return xn, tabla, mensaje
