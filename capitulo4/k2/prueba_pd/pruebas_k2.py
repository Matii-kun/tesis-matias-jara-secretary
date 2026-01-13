import sys
import os

# Permite importar desde la carpeta hermana programa_dinamico
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from programa_dinamico.pd_k2 import dynamic_programming_k2


def prueba_tiempos(N_list):
    """
    Ejecuta el programa dinámico para una lista de valores de N
    y retorna (N, valor, (r1, r2)).
    """
    resultados = []
    for N in N_list:
        valor, tiempos = dynamic_programming_k2(N)
        resultados.append((N, valor, tiempos))
    return resultados


if __name__ == "__main__":

    # Pruebas de convergencia (valores y tiempos)
    N_list = [10, 30, 100, 500, 2000]
    res = prueba_tiempos(N_list)

    for N, valor, (r1, r2) in res:
        print(f"N={N}: valor={valor:.6f}, r_1={r1}, r_2={r2}")

    # Prueba diagnóstica: se imprimen F y D solo para N pequeño
    N = 10
    valor, tiempos = dynamic_programming_k2(N, verbose=True)
    r1, r2 = tiempos
    print(f"\n[Diagnóstico] N={N}: valor={valor:.6f}, r_1={r1}, r_2={r2}")
