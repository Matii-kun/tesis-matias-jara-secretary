"""
Pruebas computacionales del programa dinámico para el Problema Pesimista con k = 2.

Se evalúa el valor óptimo y los tiempos [r1, r2, r3] para distintas elecciones
de parámetros (q1, q2, q12).

Además, se incluye una prueba detallada (verbose=True) que imprime las matrices
F y D para un N pequeño.
"""

import sys
import os

# Permite importar desde k2/programa_dinamico
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from programa_dinamico.pd_pesimista_k2 import dynamic_programming_pesimista_k2


def prueba_parametros(casos):
    """
    Ejecuta el programa dinámico para una lista de casos (N, q1, q2, q12).
    """
    for N, q1, q2, q12 in casos:
        valor, tiempos = dynamic_programming_pesimista_k2(N, q1, q2, q12)
        r1, r2, r3 = tiempos
        print(f"N={N}")
        print(f"  q1={q1}, q2={q2}, q12={q12}")
        print(f"  valor  = {valor:.6f}")
        print("  tiempos:")
        print(f"    r1 = {r1}")
        print(f"    r2 = {r2}")
        print(f"    r3 = {r3}")
        print()


if __name__ == "__main__":

    # Pruebas generales (sin verbose)
    casos = [
        (10, 0.5, 0.5, 1.0),
        (1000, 0.5, 0.5, 1.0),
        (1000, 1.0, 0.0, 1.0),
        (1000, 0.0, 1.0, 1.0),
    ]

    prueba_parametros(casos)

    # Prueba detallada (verbose=True)
    print("Prueba detallada (verbose=True):")
    N = 10
    q1, q2, q12 = 0.5, 0.5, 1.0
    valor, tiempos = dynamic_programming_pesimista_k2(N, q1, q2, q12, verbose=True)
    r1, r2, r3 = tiempos
    print(f"N={N}")
    print(f"  q1={q1}, q2={q2}, q12={q12}")
    print(f"  valor  = {valor:.6f}")
    print("  tiempos:")
    print(f"    r1 = {r1}")
    print(f"    r2 = {r2}")
    print(f"    r3 = {r3}")
