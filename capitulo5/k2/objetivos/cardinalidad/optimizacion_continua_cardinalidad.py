import numpy as np
from scipy.optimize import minimize


def objetivo_cardinalidad(t):
    """
    Función objetivo del análisis continuo para el objetivo de cardinalidad,
    en el caso k=2 (Problema Pesimista) con q1=q2=1/2 y q12=1.

    Entrada
    ------
    t : array-like de largo 3
        t = (t1, t2, t3) con 0 < t1 < t2 < t3 < 1.

    Retorna
    -------
    float
        Valor a minimizar (negativo del valor que queremos maximizar).
    """
    t1, t2, t3 = t

    # Evitar logs inválidos
    if not (0 < t1 < t2 < t3 < 1):
        return 1e9

    # Componentes de la función
    phi1 = (
        t1 * t3 * np.log(t2 / t1)
        - t1 * t2 * np.log(t2)
        + t1 * t2 * t3 * (1 / t2 - 1 / t3)
        - t1 * t2 * np.log(t3 / t2)
    )

    phi2 = -t1 * t2 * np.log(t2)

    phi12 = (
        -t1 * t3 * np.log(t3) * np.log(t2 / t1)
        - t1 * t2 * t3 * np.log(t3) * (1 / t2 - 1 / t3)
        + t1 * t2 * (np.log(t3) ** 2) / 2
    )

    phi21 = (
        t1 * (t3 * np.log(t2 / t1) - (t2 - t1))
        - t1 * t3 * np.log(t3) * np.log(t2 / t1)
        + t1 * t2 * t3 * (1 / t2 - 1 / t3)
        - t1 * t2 * np.log(t3 / t2)
        - t1 * t2 * t3 * np.log(t3) * (1 / t2 - 1 / t3)
        + t1 * t2 * (np.log(t3) ** 2) / 2
    )

    # Objetivo
    valor = phi12 + phi21 + 0.5 * phi1 + 0.5 * phi2

    return -valor


def optimizar_cardinalidad(
    initial_guess=(0.3, 0.5, 0.77),
    maxiter=2000,
    ftol=1e-14,
):
    """
    Optimiza el objetivo continuo para cardinalidad.

    Retorna
    -------
    t_opt : np.ndarray
    valor_opt : float
    result : OptimizeResult
    """

    bounds = [(1e-6, 1 - 1e-6)] * 3

    eps = 1e-8
    constraints = [
        {"type": "ineq", "fun": lambda x: x[1] - x[0] - eps},
        {"type": "ineq", "fun": lambda x: x[2] - x[1] - eps},
    ]

    result = minimize(
        objetivo_cardinalidad,
        np.array(initial_guess, dtype=float),
        bounds=bounds,
        constraints=constraints,
        method="SLSQP",
        options={"ftol": ftol, "maxiter": maxiter, "disp": True},
    )

    if not result.success:
        raise RuntimeError(f"Optimización falló: {result.message}")

    t_opt = result.x
    valor_opt = -result.fun

    return t_opt, valor_opt, result


if __name__ == "__main__":

    t_opt, val_opt, res = optimizar_cardinalidad()

    t1, t2, t3 = t_opt

    print("\nResultados (objetivo cardinalidad):")
    print(f"t1 = {t1:.10f}")
    print(f"t2 = {t2:.10f}")
    print(f"t3 = {t3:.10f}")
    print(f"valor = {val_opt:.10f}")

    print(f"\nChequeo objetivo(t_opt) = {objetivo_cardinalidad(t_opt):.10e}")
