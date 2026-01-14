import numpy as np

def dynamic_programming_k2(N, verbose=False):
    """
    Programa dinámico para el Secretary Problem pesimista con k = 2.

    Parámetros
    ----------
    N : int
        Número total de elementos.

    Retorna
    -------
    F_0 : float
        Valor óptimo del programa dinámico en el estado inicial.
    tiempos : list[int]
        Lista [r1, r2] donde:
        - r1 es el ultimo r donde se rechaza el estado (r,1,0)
        - r2 es el ultimo r donde se rechaza el estado (r,2,1)
    """

    # F[r, s, c]: función valor
    F = np.zeros((N+1, 4, 3))

    # D[r, s, c]: decisión óptima (1 = aceptar, 0 rechazar)
    D = np.zeros((N+1, 4, 3))

    # Condiciones terminales
    F[N, 1, 2] = 1
    F[N, 2, 1] = 1
    D[N, 1, 2] = 1
    D[N, 2, 1] = 1

    for r in range(N-1, 0, -1):
        for s in range(3, 0, -1):
            for c in range(2, -1, -1):

                if r == 1 and c in {1, 2}:
                    F[r, s, c] = 0

                elif r < N and s == 1 and c == 2:
                    escoger = (r-1)/(N-1) * (r/N)
                    if escoger > 0:
                        D[r, s, c] = 1
                    F[r, s, c] = escoger

                elif r < N and s == 2 and c == 1:
                    escoger = (r-1)/(N-1) * (r/N)
                    no_escoger = (
                        (1/(r+1)) * F[r+1, 1, 2]
                        + (1/(r+1)) * F[r+1, 2, 1]
                        + ((r-1)/(r+1)) * F[r+1, 3, 1]
                    )
                    if escoger > no_escoger:
                        D[r, s, c] = 1
                    F[r, s, c] = max(escoger, no_escoger)

                elif r < N and s == 1 and c == 0:
                    escoger = (
                        (1/(r+1)) * F[r+1, 1, 2]
                        + (1/(r+1)) * F[r+1, 2, 1]
                        + ((r-1)/(r+1)) * F[r+1, 3, 1]
                    )
                    no_escoger = (
                        (1/(r+1)) * F[r+1, 1, 0]
                        + (r/(r+1)) * F[r+1, 2, 0]
                    )
                    if escoger > no_escoger:
                        D[r, s, c] = 1
                    F[r, s, c] = max(escoger, no_escoger)

                elif s > 2 and r < N and c == 1:
                    F[r, s, c] = (
                        (1/(r+1)) * F[r+1, 1, 2]
                        + (1/(r+1)) * F[r+1, 2, 1]
                        + ((r-1)/(r+1)) * F[r+1, 3, 1]
                    )

                elif s == 2 and 1 < r < N and c == 0:
                    F[r, s, c] = (
                        (1/(r+1)) * F[r+1, 1, 0]
                        + (r/(r+1)) * F[r+1, 2, 0]
                    )

    # Extracción de tiempos
    tiempos = [None, None]
    for r in range(1, N+1):
        rr = r - 1
        if tiempos[0] is None and D[r, 1, 0] == 1:
            tiempos[0] = rr
        if tiempos[1] is None and D[r, 2, 1] == 1:
            tiempos[1] = rr
        if all(t is not None for t in tiempos):
            break
    if verbose==True:
      print(F[1:,:,:])
      print(D[1:,:,:])

    valor = F[1, 1, 0]  
    return valor, tiempos
