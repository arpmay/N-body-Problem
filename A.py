import numpy as np

def acceleration(r, m):
    G = 6.67*(10**(-4))  # Universal Gravitational constant
    n = len(r)
    a = np.zeros((2,n))
    for i in range(n):
        for j in range(n):
            if i != j:
                rij = r[:,i] - r[:,j]
                a[:,i] -= G * m[j] * rij / np.linalg.norm(rij)**3
    return a
