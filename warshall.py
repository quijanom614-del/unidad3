def warshall(matriz):
    n = len(matriz)
    alcance = [fila[:] for fila in matriz]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcance[i][j] = alcance[i][j] or (alcance[i][k] and alcance[k][j])

    return alcance


# -------------------- EJEMPLO --------------------
matriz = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0]
]

resultado = warshall(matriz)
print("Matriz de clausura transitiva:")
for fila in resultado:
    print(fila)
