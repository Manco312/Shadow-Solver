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
