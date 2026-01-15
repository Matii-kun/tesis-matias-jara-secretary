import sys
import os

# Permite importar desde programa_dinamico
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from programa_dinamico.pd_k_general import dynamic_programming_k_general


def prueba_pd_k_general(casos):
    """
    Ejecuta el PD general para una lista de pares (N, k).
    Retorna una lista con (N, k, valor, tiempos).
    """
    resultados = []
    for N, k in casos:
        valor, tiempos = dynamic_programming_k_general(N, k)
        resultados.append((N, k, valor, tiempos))
    return resultados


if __name__ == "__main__":

    # Casos de prueba (ajusta si quieres)
    casos = [
        (100,1),  # Problema Clasico
        (10, 2),  # Recuperamos caso k = 2
        (20, 3),
        (30, 5),
        (50, 5),
        (7, 7),   # Caso Borde
    ]

    res = prueba_pd_k_general(casos)

    for N, k, valor, tiempos in res:
        print(f"N = {N}, k = {k}")
        print(f"  valor  = {valor:.6f}")
        print(f"  tiempos:")
        for i, t in enumerate(tiempos, start=1):
            print(f"    r{i} = {t}")
        print()

    # Prueba detallada con impresión de matrices
    print("Prueba detallada (verbose=True):")
    print()
    N, k = 15, 3
    valor, tiempos = dynamic_programming_k_general(N, k, verbose=True)

    print(f"N = {N}, k = {k}")
    print(f"  valor = {valor:.6f}")
    print("  tiempos:")
    for i, r in enumerate(tiempos, start=1):
        print(f"    r{i} = {r}")
