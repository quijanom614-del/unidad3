import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        dist_actual, nodo_actual = heapq.heappop(cola)

        for vecino, peso in grafo[nodo_actual]:
            nueva_dist = dist_actual + peso
            if nueva_dist < distancias[vecino]:
                distancias[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))

    return distancias


grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [],
    'E': [('D', 4)]
}

resultado = dijkstra(grafo, 'A')
print("Distancias desde A:", resultado)
