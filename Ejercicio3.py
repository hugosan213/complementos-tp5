import numpy as np


A = np.array([
    [0.0001,1],[1,1]
], dtype=float)

B = np.array([1.0001,2], dtype=float)

# Armamos la matriz ampliada
matriz_ampliada = np.column_stack([A, B])
n = len(matriz_ampliada)

# 1. Eliminación hacia adelante (triangulación)
for i in range(n - 1):
    maximo_valor=i + np.argmax(np.abs(matriz_ampliada[i:, i]))

    if maximo_valor != i:
        matriz_ampliada[[i, maximo_valor]] = matriz_ampliada[[maximo_valor, i]]
        print(f"Intercambio de filas {i} y {maximo_valor}:")
        print(matriz_ampliada)
        print("-" * 30)
        
    for j in range(i + 1, n):
        factor = matriz_ampliada[j, i] / matriz_ampliada[i, i]
        matriz_ampliada[j] = matriz_ampliada[j] - factor * matriz_ampliada[i]

# 2. Sustitución regresiva (despeje de abajo hacia arriba)
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = matriz_ampliada[i, -1]
    
    for j in range(i + 1, n):
        x[i] -= matriz_ampliada[i, j] * x[j]
        
    x[i] /= matriz_ampliada[i, i]

# 3. Resultados
print("Matriz triangulada:")
print(matriz_ampliada)
print("\nLos valores de las incógnitas son:", x)
