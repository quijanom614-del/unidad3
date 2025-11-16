def floyd_warshall(grafo):
    dist = [fila[:] for fila in grafo] 

    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist



INF = 9999
grafo = [
    [0, 4, INF],
    [INF, 0, 3],
    [2, INF, 0]
]

resultado = floyd_warshall(grafo)
print("Matriz de distancias mínima:")
for fila in resultado:
    print(fila)
