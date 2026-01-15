"""
Genera las figuras del Capítulo 4 correspondientes al caso de rango general k.

Este script compara:
- el valor óptimo del programa dinámico PD(N, k),
- y los tiempos normalizados r_i(N)/N,

con los valores límite t_i y P_k obtenidos por Lehtinen mediante un
enfoque analítico distinto.

En particular, se estudia el caso k = 5 y se visualiza la convergencia
cuando N → ∞.
"""

import sys
import os

# Permite importar desde programa_dinamico_general
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from programa_dinamico_general.pd_k_general import dynamic_programming_k_general

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Valores de Lehtinen:
t1 = 0.10789
t2 = 0.28073
t3 = 0.45863
t4 = 0.63822
t5 = 0.81873

P5 = 0.104305

# ------------------------------
# Ahora graficamos

# Generemos valores simulados del programa dinámico

PD_values = []
r1_values = []
r2_values = []
r3_values = []
r4_values = []
r5_values = []

N = 200
n_values = np.arange(5, N+1, 1)
for i in n_values:
    v, r = dynamic_programming_k_general(i,5)
    PD_values.append(v)
    r1_values.append(r[0]/i)
    r2_values.append(r[1]/i)
    r3_values.append(r[2]/i)
    r4_values.append(r[3]/i)
    r5_values.append(r[4]/i)

fig, axs = plt.subplots(2, 1, figsize=(8,8))

# Gráfico 1: PD vs P2
axs[0].plot(n_values, PD_values, label='PD(N,5)', color='b')
axs[0].axhline(P5, color='r', linestyle='--', label=f'$P_5 \\approx {P5:.6f}$')
axs[0].set_xlabel('$N$')
axs[0].set_ylabel('$\\mathrm{PD}(N)$')
#axs[0].set_title(rf'Comparación $\mathrm{{PD}}(N,5)$ con $P_5$ hasta $N_{max}={N}$')
#axs[0].set_title(rf'Comparación $\mathrm{{PD}}(N,5)$ con $P_5$ hasta $N_{{\max}}={N}$')
axs[0].set_title(rf'Convergencia del valor óptimo $\mathrm{{PD}}(N,5)$ hacia $P_5$')


axs[0].legend()
axs[0].grid(True)

# Curvas r_i(N)/N con tus colores originales
lwp = 1.2
axs[1].plot(n_values, r1_values, label='$r_1(N)/N$', color='green',linewidth=1.2, alpha=0.8)
axs[1].plot(n_values, r2_values, label='$r_2(N)/N$', color='magenta',linewidth=1.2, alpha=0.8)
axs[1].plot(n_values, r3_values, label='$r_3(N)/N$', color='brown',linewidth=1.2, alpha=0.8)
axs[1].plot(n_values, r4_values, label='$r_4(N)/N$', color='purple',linewidth=1.2, alpha=0.8)
axs[1].plot(n_values, r5_values, label='$r_5(N)/N$', color='cyan',linewidth=1.2, alpha=0.8)


# Líneas horizontales t_i con colores distintos a todas las curvas y entre sí
axs[1].axhline(t1, color='red', linestyle='--', label=f'$t_1 \\approx {t1:.5f}$',linewidth=1.2)
axs[1].axhline(t2, color='blue', linestyle='--', label=f'$t_2 \\approx {t2:.5f}$',linewidth=1.2)
axs[1].axhline(t3, color='black', linestyle='--', label=f'$t_3 \\approx {t3:.5f}$',linewidth=1.2)
axs[1].axhline(t4, color='darkorange', linestyle='--', label=f'$t_4 \\approx {t4:.5f}$',linewidth=1.2)
axs[1].axhline(t5, color='darkgreen', linestyle='--', label=f'$t_5 \\approx {t5:.5f}$',linewidth=1.2)

#axs[1].legend(handles=custom_legend, ncol=2, loc='best')

axs[1].set_xlabel('$N$')
axs[1].set_ylabel('Tiempos normalizados')
axs[1].set_title('Comparación de $r_i$ a $t_i$, tiempos obtenidos por Lehtinen')
axs[1].set_title('Convergencia de los tiempos normalizados $r_i(N)/N$ hacia los valores $t_i$')

axs[1].legend(ncol=2, loc='upper right', fontsize=9)
axs[1].grid(True)

plt.tight_layout()
plt.show()
