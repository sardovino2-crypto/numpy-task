import numpy as np

# Controlla il file readme.md per i dettagli su ciascun sub-task

def prodotto_scalare(v1: list, v2: list) -> float:
    """Sub-task 1: Prodotto Scalare."""
    a=np.array(v1)
    b=np.array(v2)
    c=np.dot(a,b)
    return c

def rango_matrice(m: list) -> int:
    """Sub-task 2: Calcola il rango di una matrice."""
    matr=np.array(m)
    r=np.linalg.matrix_rank(matr)
    return r


def risolvi_sistema_lineare(A: list, b: list) -> np.ndarray:
    """Sub-task 3: Risolvere un Sistema Lineare."""
    matr = np.array(A)
    vett = np.array(b)
    r=np.linalg.solve(matr, vett)
    return r

def correlazione_matrici(m1: list, m2: list) -> np.ndarray:
    """Sub-task 4: Correlazione tra Matrici 2x2."""
    pass



def operazioni_elemento_per_elemento(v1: list) -> tuple:
    """Sub-task 5: Restituisce (seno, coseno, arcoseno, arcocoseno) elemento per elemento calcolati sul primo array."""
    v=np.array(v1)
    v1=np.sin(v)
    v2=np.cos(v)
    v3=np.arcsin(v)
    v4=np.arccos(v)
    result=list([v1, v2, v3, v4])
    return result



def main():
    print("Sub-task 1:", prodotto_scalare([1, 2, 3], [4, 5, 6]))
    print("Sub-task 1:", rango_matrice([[1, 2], [3, 4]]))
    print("Sub-task 3:", risolvi_sistema_lineare([[2, 1], [1, 3]], [5, 7]))
    print("Sub-task 4:", correlazione_matrici([[1, 2], [3, 4]], [[2, 4], [6, 8]]))
    print("Sub-task 5:", operazioni_elemento_per_elemento([0, 0.5, 1, -0.5]))

if __name__ == "__main__":
    main()
