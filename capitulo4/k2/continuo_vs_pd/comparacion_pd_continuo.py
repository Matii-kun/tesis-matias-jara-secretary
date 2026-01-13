"""
Genera las figuras del Capítulo 4 correspondientes a la comparación
entre el programa dinámico y el análisis continuo.
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Permite importar desde programa_dinamico
#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#from programa_dinamico.pd_k2 import dynamic_programming_k2


# Valores óptimos del análisis continuo
# (obtenidos ejecutando optimizacion_continua.py)
t1 = 0.2291145241
t2 = 0.6065308503
P2 = 0.2254366561


# ------------------------------
# Graficamos el caso k = 2

PD_values = []
r1_values = []
r2_values = []

N = 200
n_values = np.arange(3, N + 1, 1)   # desde 2 hasta N (incluye N)

for i in n_values:
    v, r = dynamic_programming_k2(i)
    if i==2:
        PD_values.append(v)
        r1_values.append(0/i)
        r2_values.append(1/i)
    else:    
        PD_values.append(v)
        r1_values.append((r[0]) / i)
        r2_values.append((r[1]) / i)

fig, axs = plt.subplots(2, 1, figsize=(8, 8))

# ---------------- Gráfico 1: PD(N,2) vs P2 ----------------
axs[0].plot(n_values, PD_values, label='PD(N,2)', color='b')
axs[0].axhline(P2, color='r', linestyle='--',
               label=f'$P_2 \\approx {P2:.6f}$')

axs[0].set_xlabel('$N$')
axs[0].set_ylabel('$\\mathrm{PD}(N)$')
axs[0].set_title(
    r'Convergencia del valor óptimo $\mathrm{PD}(N)$ hacia $P_2$'
)

axs[0].legend()
axs[0].grid(True)

# ---------------- Gráfico 2: r_i(N)/N vs t_i ----------------
axs[1].plot(n_values, r1_values, label='$r_1(N)/N$', color='green')
axs[1].plot(n_values, r2_values, label='$r_2(N)/N$', color='purple')

axs[1].axhline(t1, color='orange', linestyle='--',
               label=f'$t_1 \\approx {t1:.4f}$')
axs[1].axhline(t2, color='skyblue', linestyle='--',
               label=f'$t_2 \\approx {t2:.4f}$')

axs[1].set_xlabel('$N$')
axs[1].set_ylabel('Tiempos normalizados')
axs[1].set_title(
    'Convergencia de los tiempos normalizados '
    '$r_i(N)/N$ hacia los valores $t_i$'
)

axs[1].legend(ncol=2, loc='best', fontsize=9)
axs[1].grid(True)

plt.tight_layout()
plt.show()
