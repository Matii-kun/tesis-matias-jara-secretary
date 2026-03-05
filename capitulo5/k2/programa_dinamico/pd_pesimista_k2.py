import numpy as np

def dynamic_programming_pesimista_k2(N, q1, q2, q12, verbose=False):
    """
    Programa dinámico para el Problema Pesimista con k = 2.

    Parámetros
    ----------
    N : int
        Número total de elementos.
    q1 : float
        Recompensa por seleccionar {e1}.
    q2 : float
        Recompensa por seleccionar {e2}.
    q12 : float
        Recompensa por seleccionar {e1,e2}.

    Retorna
    -------
    F_0 : float
        Valor óptimo del programa dinámico en el estado inicial.
    tiempos : list[int]
        Lista [r1, r2, r3] donde:
        - r1 es el ultimo r donde se rechaza el estado (r,1,0)
        - r2 es el ultimo r donde se rechaza el estado (r,2,0)
        - r3 es el ultimo r donde se rechaza el estado (r,2,1)
    """

    F = np.zeros((N+1,4,3))
    D = np.zeros((N+1,4,3))

    if q12 > 0:
        D[N,1,2] = 1
        D[N,2,1] = 1

    if q1 > 0:
        D[N,1,0] = 1

    if q2 > 0:
        D[N,2,0] = 1

    D[N,3,1] = 0
    D[N,3,2] = 0
    
    # Casos bordes
    F[N,1,2] = q12
    F[N,2,1] = q12
    F[N,1,0] = q1
    F[N,2,0] = q2
    F[N,3,1] = q1
    F[N,3,2] = q2

    # En el resto de casos el valor es 0

    for r in range(N-1,0,-1):
        for s in range(3,-1,-1):
            for c in range(2,-1,-1):

                # Algunos estados del programa dinámico no existen
                # (por ejemplo r=1 con c=1 o c=2). Estos estados no afectan
                # la recursión y quedan con valor 0 por la inicialización.

                if r < N and s == 1 and c == 2:

                    escoger = q12 * ((r-1)/(N-1)) * (r/N)
                    no_escoger = 0

                    if escoger > no_escoger:
                        D[r,s,c] = 1

                    F[r,s,c] = escoger

                elif r < N and s == 2 and c == 2:
                    # No existe
                    F[r,s,c] = 0

                elif r < N and s == 2 and c == 1:

                    escoger = q12 * ((r-1)/(N-1)) * (r/N)

                    no_escoger = (
                        (1/(r+1))*F[r+1,1,2]
                        + (1/(r+1))*F[r+1,2,1]
                        + ((r-1)/(r+1))*F[r+1,3,1]
                    )

                    if escoger > no_escoger:
                        D[r,s,c] = 1

                    F[r,s,c] = max(escoger,no_escoger)

                elif r < N and s == 1 and c == 0:

                    escoger = (
                        (1/(r+1))*F[r+1,1,2]
                        + (1/(r+1))*F[r+1,2,1]
                        + ((r-1)/(r+1))*F[r+1,3,1]
                    )

                    no_escoger = (
                        (1/(r+1))*F[r+1,1,0]
                        + (1/(r+1))*F[r+1,2,0]
                        + ((r-1)/(r+1))*F[r+1,3,0]
                    )

                    if escoger > no_escoger:
                        D[r,s,c] = 1

                    F[r,s,c] = max(escoger,no_escoger)

                elif s == 3 and 2 < r < N and c == 1:

                    F[r,s,c] = (
                        (1/(r+1))*F[r+1,1,2]
                        + (1/(r+1))*F[r+1,2,1]
                        + ((r-1)/(r+1))*F[r+1,3,1]
                    )

                elif s == 2 and 1 < r < N and c == 0:

                    escoger = (
                        (1/(r+1))*0
                        + (1/(r+1))*0
                        + ((r-1)/(r+1))*F[r+1,3,2]
                    )

                    no_escoger = (
                        (1/(r+1))*F[r+1,1,0]
                        + (1/(r+1))*F[r+1,2,0]
                        + ((r-1)/(r+1))*F[r+1,3,0]
                    )

                    if escoger > no_escoger:
                        D[r,s,c] = 1

                    F[r,s,c] = max(escoger,no_escoger)

                elif s == 3 and 2 < r < N and c == 2:

                    F[r,s,c] = (
                        (1/(r+1))*0
                        + (1/(r+1))*0
                        + ((r-1)/(r+1))*F[r+1,3,2]
                    )

                elif s == 3 and 2 < r < N and c == 0:

                    F[r,s,c] = (
                        (1/(r+1))*F[r+1,1,0]
                        + (1/(r+1))*F[r+1,2,0]
                        + ((r-1)/(r+1))*F[r+1,3,0]
                    )

    tiempos = [None,None,None]

    for r in range(3,N+1):

        rr = r-1

        if tiempos[0] is None and D[r,1,0] == 1:
            tiempos[0] = rr

        if tiempos[1] is None and D[r,2,0] == 1:
            tiempos[1] = rr

        if tiempos[2] is None and D[r,2,1] == 1:
            tiempos[2] = rr

        if all(t is not None for t in tiempos):
            break

    if verbose:

        print("Matrices de valores F")
        print(F[1:,:,:])
        print()

        print("Matrices de decisiones D")
        print(D[1:,:,:])
        print()

    valor = F[1,1,0]

    return valor, tiempos
