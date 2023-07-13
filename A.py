from numpy import sqrt

def acceleration(q, m, i):
    n = len(q)
    A = 0
    B = 0
    for j in range(n):
        if j == i:
            continue
        dist = sqrt((q[0][i] - q[0][j])**2 + (q[1][i] - q[1][j])**2)
        A = A + (m[j]*(q[0][j] - q[0][i]))/(dist**3)
        B = B + (m[j]*(q[1][j] - q[1][i]))/(dist**3)
    return [A, B]