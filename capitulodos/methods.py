import numpy as np

def jacobi(x0, A, b, tol, niter, cs):
    x0 = np.array(x0, dtype=float)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    T = np.linalg.inv(D).dot(L + U)
    C = np.linalg.inv(D).dot(b)
    error = tol + 1
    c = 0
    
    # Store x0 as a list, not unpacked
    tabla = [(c, x0.tolist(), None)]

    while error > tol and c < niter:
        x1 = T.dot(x0) + C
        if cs:
            denominador = np.linalg.norm(x1, ord=np.inf)
            if denominador == 0:
                error = float('inf')
            else:
                error = np.linalg.norm(x1 - x0, ord=np.inf) / denominador
        else:
            error = np.linalg.norm(x1 - x0, ord=np.inf)
        c += 1
        
        # Store x1 as a list, not unpacked
        tabla.append((c, x1.tolist(), error))
        x0 = x1

    if error < tol:
        mensaje = f"La solución se encontró con tolerancia {tol} en {c} iteraciones"
    else:
        mensaje = f"Fracasó en {niter} iteraciones"

    return tabla, mensaje


def gauss_seidel(x0, A, b, tol, niter, cs):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x0 = np.array(x0, dtype=float)
    
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)

    try:
        inv_DL = np.linalg.inv(D - L)
    except np.linalg.LinAlgError:
        return [], "Error: No se puede invertir D - L (puede no ser invertible)."

    T = np.matmul(inv_DL, U)
    C = np.matmul(inv_DL, b)

    tabla = []
    error = tol + 1
    contador = 0
    x_act = x0

    while error > tol and contador < niter:
        x_sig = np.matmul(T, x_act) + C

        if cs:
            denominador = np.linalg.norm(x_sig, ord=np.inf)
            if denominador == 0:
                error = float('inf')
            else:
                error = np.linalg.norm(x_sig - x_act, ord=np.inf) / denominador
        else:
            error = np.linalg.norm(x_sig - x_act, ord=np.inf)

        tabla.append([contador + 1, x_sig.tolist(), round(error, 10) if contador > 0 else None])
        x_act = x_sig
        contador += 1

    if error <= tol:
        mensaje = f"Aproximación encontrada: {x_act.tolist()} con tolerancia {tol}"
    else:
        mensaje = f"Fracasó en {niter} iteraciones. Última aproximación: {x_act.tolist()}"

    return tabla, mensaje

def sor(x0, A, b, tol, niter, w, cs):
    """
    Método SOR para resolver Ax = b.
    
    Parámetros:
    x0: vector inicial
    A: matriz de coeficientes
    b: vector de términos independientes
    tol: tolerancia para el error
    niter: número máximo de iteraciones
    w: factor de relajación (0 < w < 2)
    cs: si True calcula error relativo, si False absoluto
    
    Retorna:
    tabla: lista con filas [iteración, vector x, error]
    mensaje: string con resultado de la convergencia
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    x0 = np.array(x0, dtype=float)

    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)

    try:
        inv_term = np.linalg.inv(D - w * L)
    except np.linalg.LinAlgError:
        return [], "Error: No se puede invertir (D - w*L), matriz singular o no invertible."

    T = inv_term @ ((1 - w) * D + w * U)
    C = w * inv_term @ b

    tabla = []
    error = tol + 1
    contador = 0
    x_act = x0

    while error > tol and contador < niter:
        x_sig = T @ x_act + C

        if cs:
            denom = np.linalg.norm(x_sig, ord=np.inf)
            if denom == 0:
                error = float('inf')
            else:
                error = np.linalg.norm(x_sig - x_act, ord=np.inf) / denom
        else:
            error = np.linalg.norm(x_sig - x_act, ord=np.inf)

        tabla.append([contador + 1, x_sig.tolist(), round(error, 10) if contador > 0 else None])
        x_act = x_sig
        contador += 1

    if error <= tol:
        mensaje = f"Aproximación encontrada en {contador} iteraciones con tolerancia {tol}."
    else:
        mensaje = f"Fracasó en {niter} iteraciones. Última aproximación: {x_act.tolist()}"

    return tabla, mensaje
