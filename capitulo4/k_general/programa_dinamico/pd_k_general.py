import numpy as np
import math

def product_fractions_math(r, n, k):
    r"""
    Producto \prod_{i=0}^{k-1} (r - i)/(n - i).
    Aparece en términos de última aceptación.
    """
    return math.prod((r - i) / (n - i) for i in range(k))


def dynamic_programming_k_general(N, k, verbose=False):
    """
    Programa dinámico para el problema Todo o nada
    en el caso de rango general k.

    Parámetros
    ----------
    N : int
        Número total de elementos.
    k : int
        Rango del matroide uniforme.
    verbose : bool, optional
        Si True, imprime las matrices F y D.

    Retorna
    -------
    valor : float
        Valor óptimo del programa dinámico en el estado inicial.
    tiempos : list[int]
        Vector de tamaño k, donde tiempos[i] es el último r
        tal que se rechaza el estado (r, i+1, i).

    """

    # F[r, s, c]: función valor
    F = np.zeros((N + 1, k + 2, k))

    # D[r, s, c]: decisión óptima (1 = aceptar, 0 = rechazar)
    D = np.zeros((N + 1, k + 2, k))

    # Condiciones terminales
    for i in range(1, k + 1):
        F[N, i, k - 1] = 1
        D[N, i, k - 1] = 1

    # Programa dinámico
    for r in range(N - 1, 0, -1):
        for s in range(k + 1, 0, -1):
            for c in range(k - 1, -1, -1):

                ### Caso de decisión no directa (aceptar o rechazar) ###
                if s == c + 1 and s < k:
                    escoger = (
                        (1 / (r + 1)) * sum(F[r + 1, i, c + 1] for i in range(1, s + 2))
                        + ((r - c - 1) / (r + 1)) * F[r + 1, s + 2, c + 1]
                    )
                    no_escoger = (
                        (1 / (r + 1)) * sum(F[r + 1, i, c] for i in range(1, s + 1))
                        + ((r - c) / (r + 1)) * F[r + 1, s + 1, c]
                    )
                    F[r, s, c] = max(escoger, no_escoger)
                    if escoger > no_escoger:
                        D[r, s, c] = 1

                # Última aceptación posible
                elif c == k - 1 and s == k:
                    escoger = product_fractions_math(r, N, k)
                    no_escoger = (
                        (1 / (r + 1)) * sum(F[r + 1, i, c] for i in range(1, k + 1))
                        + ((r + 1 - k) / (r + 1)) * F[r + 1, k + 1, c]
                    )
                    F[r, s, c] = max(escoger, no_escoger)
                    if escoger > no_escoger and r > 1:
                        D[r, s, c] = 1

                ### Siempre aceptar ###
                elif s <= c and c < k - 1:
                    escoger = (
                        (1 / (r + 1)) * sum(F[r + 1, i, c + 1] for i in range(1, c + 3))
                        + ((r - c - 1) / (r + 1)) * F[r + 1, c + 3, c + 1]
                    )
                    F[r, s, c] = escoger
                    if escoger > 0:
                        D[r, s, c] = 1
                
                # Caso borde (ultima elección)
                elif s < k and c == k - 1:
                    escoger = product_fractions_math(r, N, k)
                    F[r, s, c] = escoger
                    if escoger > 0:
                        D[r, s, c] = 1        

                ### Siempre rechazar ###
                elif s == c + 2:
                    no_escoger = (
                        (1 / (r + 1)) * sum(F[r + 1, i, c] for i in range(1, c + 2))
                        + ((r - c) / (r + 1)) * F[r + 1, c + 2, c]
                    )
                    F[r, s, c] = no_escoger

    # Extracción de tiempos r_i
    tiempos = [None] * k
    for i in range(1, k + 1):
        for r in range(1, N + 1):
            if tiempos[i - 1] is None and D[r, i, i - 1] == 1:
                tiempos[i - 1] = r - 1
                break

    if verbose:
        print(F)
        print(D)

    valor = F[1, 1, 0]
    return valor, tiempos
