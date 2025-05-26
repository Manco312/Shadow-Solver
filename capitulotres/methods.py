import numpy as np

def vandermonde_interpolation(x, y):
    # Calcular matriz de Vandermonde y resolver
    A = np.vander(x, increasing=False)
    a = np.linalg.solve(A, y)

    # Construcción del polinomio como string
    poly_str = "P(x) = "
    degree = len(a) - 1
    terms = []
    for i, coef in enumerate(a):
        power = degree - i
        terms.append(f"{coef:.6f}x^{power}" if power > 1 else
                     f"{coef:.6f}x" if power == 1 else
                     f"{coef:.6f}")
    poly_str += " + ".join(terms)

    # Evaluar el polinomio en un intervalo para graficar
    xpol = np.linspace(min(x), max(x), 500)
    p = np.polyval(a, xpol)

    # Eliminar un punto aleatorio y recalcular
    if len(x) > 2:
        index_to_remove = np.random.randint(0, len(x))
        x_reduced = np.delete(x, index_to_remove)
        y_reduced = np.delete(y, index_to_remove)
        A_reduced = np.vander(x_reduced, increasing=False)
        a_reduced = np.linalg.solve(A_reduced, y_reduced)

        y_est = np.polyval(a_reduced, x[index_to_remove])
        error = abs(y[index_to_remove] - y_est)
        mensaje_error = (f"Se eliminó el punto x = {x[index_to_remove]:.2f}. "
                         f"El valor estimado con la nueva interpolación es y = {y_est:.4f}, "
                         f"el valor real era y = {y[index_to_remove]:.4f}, "
                         f"error = {error:.4f}")
    else:
        mensaje_error = "No se puede eliminar un punto si solo hay dos."

    return a, poly_str, xpol, p, mensaje_error


def newton_interpolation(x, y):
    n = len(x)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i+1][j-1] - diff_table[i][j-1]) / (x[i+j] - x[i])

    coef = diff_table[0, :]

    poly_str = f"P(x) = {coef[0]:.6f}"
    for i in range(1, n):
        term = "".join([f"(x - {x[j]:.6f})" for j in range(i)])
        poly_str += f" + ({coef[i]:.6f})*{term}"

    def eval_newton_poly(val, coef, x_points):
        result = coef[0]
        for i in range(1, len(coef)):
            term = coef[i]
            for j in range(i):
                term *= (val - x_points[j])
            result += term
        return result

    xpol = np.linspace(min(x), max(x), 500)
    p = [eval_newton_poly(xi, coef, x) for xi in xpol]

    # Calcular error al eliminar un punto (sin recursividad)
    if n > 2:
        index_to_remove = np.random.randint(0, n)
        x_reduced = np.delete(x, index_to_remove)
        y_reduced = np.delete(y, index_to_remove)

        # Calcular coeficientes del polinomio reducido
        m = len(x_reduced)
        diff_table_reduced = np.zeros((m, m))
        diff_table_reduced[:, 0] = y_reduced
        for j in range(1, m):
            for i in range(m - j):
                diff_table_reduced[i][j] = (diff_table_reduced[i+1][j-1] - diff_table_reduced[i][j-1]) / (x_reduced[i+j] - x_reduced[i])
        coef_reduced = diff_table_reduced[0, :]

        # Evaluar polinomio reducido en el punto eliminado
        y_est = eval_newton_poly(x[index_to_remove], coef_reduced, x_reduced)
        error = abs(y[index_to_remove] - y_est)
        mensaje_error = (f"Se eliminó el punto x = {x[index_to_remove]:.2f}. "
                         f"El valor estimado con la nueva interpolación es y = {y_est:.4f}, "
                         f"el valor real era y = {y[index_to_remove]:.4f}, "
                         f"error = {error:.4f}")
    else:
        mensaje_error = "No se puede eliminar un punto si solo hay dos."

    return coef, poly_str, xpol, p, mensaje_error

def lagrange_interpolation(x, y):
    def L(k, x_val):
        terms = [(x_val - x[j])/(x[k] - x[j]) for j in range(len(x)) if j != k]
        return np.prod(terms)

    def P(x_val):
        return sum(y[k] * L(k, x_val) for k in range(len(x)))

    # Construir string del polinomio simbólicamente
    # Esto es complejo para polinomio Lagrange general, aquí simplificamos imprimiendo términos base
    poly_terms = []
    n = len(x)
    for k in range(n):
        term = f"{y[k]:.6f} * "
        term += " * ".join([f"(x - {x[j]:.2f})/({x[k]:.2f} - {x[j]:.2f})" for j in range(n) if j != k])
        poly_terms.append(term)
    poly_str = "P(x) = " + " + ".join(poly_terms)

    # Evaluar el polinomio en un rango para graficar
    xpol = np.linspace(min(x), max(x), 500)
    p = np.array([P(val) for val in xpol])

    # Quitar un punto aleatorio y recalcular
    if len(x) > 2:
        index_to_remove = np.random.randint(0, len(x))
        x_reduced = np.delete(x, index_to_remove)
        y_reduced = np.delete(y, index_to_remove)

        def L_reduced(k, x_val):
            terms = [(x_val - x_reduced[j])/(x_reduced[k] - x_reduced[j]) for j in range(len(x_reduced)) if j != k]
            return np.prod(terms)

        def P_reduced(x_val):
            return sum(y_reduced[k] * L_reduced(k, x_val) for k in range(len(x_reduced)))

        y_est = P_reduced(x[index_to_remove])
        error = abs(y[index_to_remove] - y_est)
        mensaje_error = (f"Se eliminó el punto x = {x[index_to_remove]:.2f}. "
                         f"Valor estimado: y = {y_est:.4f}, "
                         f"valor real: y = {y[index_to_remove]:.4f}, "
                         f"error = {error:.4f}")
    else:
        mensaje_error = "No se puede eliminar un punto si solo hay dos."

    return poly_str, xpol, p, mensaje_error