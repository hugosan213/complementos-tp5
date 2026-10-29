import numpy as np

# 1. Definimos la matriz de coeficientes A y los tres vectores independientes
A = np.array([
    [4, 1, 1],
    [2, 5, 1],
    [1, 1, 3]
], dtype=float)

# Agrupamos los vectores b en una matriz B donde cada columna es un b_i
# Esto nos permite resolver los tres sistemas de una sola pasada de forma elegante
B_matrix = np.array([
    [9, -2, 8],
    [15, 0, 0],
    [12, 5, 4]
], dtype=float)

n = len(A)

# 2. Inicializamos L como la matriz identidad y U como una copia de A
L = np.eye(n, dtype=float)
U = A.copy()

# Proceso de Factorización LU (guardando los multiplicadores en L)
for i in range(n - 1):
    for j in range(i + 1, n):
        factor = U[j, i] / U[i, i]
        L[j, i] = factor  # Guardamos el multiplicador en L
        U[j] = U[j] - factor * U[i]  # Modificamos U

print("Matriz L (Inferior):")
print(L)
print("\nMatriz U (Superior / Triangulada):")
print(U)
print("-" * 40)

# 3. Resolvemos L * y = b para cada columna de B_matrix
# Creamos una matriz para guardar las soluciones finales x de cada sistema
resultados = np.zeros_like(B_matrix)

for k in range(B_matrix.shape[1]):  # Iteramos por cada vector b (columna)
    b = B_matrix[:, k]
    
    # Paso A: Sustitución hacia adelante para L * y = b
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]
        y[i] /= L[i, i]  # L[i,i] es siempre 1 porque es la identidad
        
    # Paso B: Sustitución hacia atrás para U * x = y
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]
        
    resultados[:, k] = x

# 4. Mostramos los resultados finales para cada sistema
print("Soluciones para cada sistema:")
print(f"Sistema 1 (para b1): x = {resultados[:, 0]}")
print(f"Sistema 2 (para b2): x = {resultados[:, 1]}")
print(f"Sistema 3 (para b3): x = {resultados[:, 2]}")