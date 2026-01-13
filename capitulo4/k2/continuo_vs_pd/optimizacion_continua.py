"""
Optimización del valor del algoritmo continuo para k = 2.

Este script se utiliza para obtener los valores óptimos (t1, t2, P2)
que luego se usan explícitamente en comparacion_pd_continuo.py.
"""

import numpy as np
from scipy.optimize import minimize


def objective(vars):
    t1, t2 = vars
    suma = (
        -2 * t1 * t2 * np.log(t2) * (np.log(t2 / t1))
        + t1 * (2 - 3 * t2 + 3 * t2 * np.log(t2) + t1 - t2 * np.log(t1))
    )
    return -suma  # minimizamos -suma para maximizar suma


def constraint_t1_le_t2(vars):
    t1, t2 = vars
    return t2 - t1  # queremos t2 - t1 >= 0


constraints = [{"type": "ineq", "fun": constraint_t1_le_t2}]
bounds = [(1e-3, 1.0), (1e-3, 1.0)]
initial_guess = [0.2, 0.6]

result = minimize(
    objective,
    initial_guess,
    bounds=bounds,
    constraints=constraints,
    options={"maxiter": 3000, "ftol": 1e-10},
)

if result.success:
    t1, t2 = result.x
    P2 = -result.fun
    print(f"t1 = {t1:.10f}")
    print(f"t2 = {t2:.10f}")
    print(f"P2 = {P2:.10f}")
else:
    print("Optimization failed:", result.message)
