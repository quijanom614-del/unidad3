class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    def union(self, x, y):
        raizX = self.find(x)
        raizY = self.find(y)
        if raizX != raizY:
            if self.rango[raizX] < self.rango[raizY]:
                self.padre[raizX] = raizY
            else:
                self.padre[raizY] = raizX
                if self.rango[raizX] == self.rango[raizY]:
                    self.rango[raizX] += 1
            return True
        return False


def kruskal(aristas, n):
    aristas.sort(key=lambda x: x[2])  # (u, v, peso)
    uf = UnionFind(n)
    mst = []

    for u, v, w in aristas:
        if uf.union(u, v):
            mst.append((u, v, w))

    return mst


aristas = [
    (0, 1, 4),  # A-B
    (0, 2, 3),  # A-C
    (1, 2, 1),  # B-C
    (1, 3, 2),  # B-D
    (2, 3, 4)   # C-D
]

resultado = kruskal(aristas, 4)
print("Árbol de expansión mínima (MST):")
for edge in resultado:
    print(edge)
