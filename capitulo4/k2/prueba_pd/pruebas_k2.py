import sys
import os

# Permite importar desde la carpeta hermana programa_dinamico
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from programa_dinamico.pd_k2 import dynamic_programming_k2


def prueba_tiempos(N_list):
    resultados = []
    for N in N_list:
        valor, tiempos = dynamic_programming_k2(N)
        resultados.append((N, valor, tiempos))
    return resultados


if __name__ == "__main__":
    N_list = [10, 30, 100, 500, 2000]
    res = prueba_tiempos(N_list)

    for N, valor, tiempos in res:
        r1, r2 = tiempos
        print(f"N = {N}")
        print(f"  valor  = {valor:.6f}")
        print(f"  tiempos:")
        print(f"    r1 = {r1}")
        print(f"    r2 = {r2}")
        print()

    # Prueba mostrando matrices F y D
    N = 10
    valor, tiempos = dynamic_programming_k2(N, verbose=True)
    r1, r2 = tiempos

    print("Prueba detallada (verbose=True)")
    print(f"N = {N}")
    print(f"  valor  = {valor:.6f}")
    print(f"  tiempos:")
    print(f"    r1 = {r1}")
    print(f"    r2 = {r2}")
