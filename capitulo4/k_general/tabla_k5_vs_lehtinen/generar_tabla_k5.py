"""
Verificación numérica de los tiempos asintóticos de Lehtinen
mediante el programa dinámico para N grande.

Se generan los valores r_i(N)/N utilizados en la tabla final
del Capítulo 4 para el caso k = 5.
"""

import sys
import os

# Permite importar desde programa_dinamico_general
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from programa_dinamico_general.pd_k_general import dynamic_programming_k_general

# Parámetros
N = 10**6
k = 5

# Ejecución del programa dinámico
valor, tiempos = dynamic_programming_k_general(N, k)

# Impresión de resultados
print("Tiempos normalizados r_i(N)/N:")
for i, r in enumerate(tiempos, start=1):
    print(f"t_{i} ≈ {r/N:.5f}")
