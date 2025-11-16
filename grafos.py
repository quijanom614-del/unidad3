import networkx as nx
import matplotlib.pyplot as plt

class Arista:
    def __init__(self, origen, destino, objeto=None, dirigida=False):
        self.origen = origen
        self.destino = destino
        self.objeto = objeto
        self.dirigida = dirigida


class Grafo:
    def __init__(self):
        self.vertices = []
        self.aristas = []

    # =====================
    #  OPERACIONES GENERALES
    # =====================
    def numVertices(self):
        return len(self.vertices)

    def numAristas(self):
        return len(self.aristas)

    def vertices(self):
        return self.vertices

    def aristas(self):
        return [(a.origen, a.destino) for a in self.aristas]

    def grado(self, v):
        return sum(1 for a in self.aristas if v in (a.origen, a.destino))

    def verticesAdyacentes(self, v):
        ady = set()
        for a in self.aristas:
            if a.origen == v:
                ady.add(a.destino)
            elif a.destino == v:
                ady.add(a.origen)
        return list(ady)

    def aristasIncidentes(self, v):
        return [(a.origen, a.destino) for a in self.aristas if v in (a.origen, a.destino)]

    def verticesFinales(self, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                return (a.origen, a.destino)
        return None

    def opuesto(self, v, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                if a.origen == v:
                    return a.destino
                elif a.destino == v:
                    return a.origen
        return None

    def esAdyacente(self, v, w):
        return any((a.origen == v and a.destino == w) or (a.origen == w and a.destino == v) for a in self.aristas)

    # ================================
    #   OPERACIONES CON ARISTAS DIRIGIDAS
    # ================================
    def aristasDirigidas(self):
        return [(a.origen, a.destino) for a in self.aristas if a.dirigida]

    def aristasNoDirigidas(self):
        return [(a.origen, a.destino) for a in self.aristas if not a.dirigida]

    def gradoEnt(self, v):
        return sum(1 for a in self.aristas if a.dirigida and a.destino == v)

    def gradoSalida(self, v):
        return sum(1 for a in self.aristas if a.dirigida and a.origen == v)

    def aristasIncidentesEnt(self, v):
        return [(a.origen, a.destino) for a in self.aristas if a.dirigida and a.destino == v]

    def aristasIncidentesSal(self, v):
        return [(a.origen, a.destino) for a in self.aristas if a.dirigida and a.origen == v]

    def verticesAdyacentesEnt(self, v):
        return [a.origen for a in self.aristas if a.dirigida and a.destino == v]

    def verticesAdyacentesSal(self, v):
        return [a.destino for a in self.aristas if a.dirigida and a.origen == v]

    def destino(self, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                return a.destino
        return None

    def origen(self, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                return a.origen
        return None

    def esDirigida(self, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                return a.dirigida
        return False

    # ================================
    #   OPERACIONES PARA ACTUALIZAR GRAFOS
    # ================================
    def insertaVertice(self, o):
        self.vertices.append(o)

    def insertaArista(self, v, w, o=None):
        self.aristas.append(Arista(v, w, o, dirigida=False))

    def insertaAristaDirigida(self, v, w, o=None):
        self.aristas.append(Arista(v, w, o, dirigida=True))

    def eliminaVertice(self, v):
        self.vertices.remove(v)
        self.aristas = [a for a in self.aristas if v not in (a.origen, a.destino)]

    def eliminaArista(self, e):
        self.aristas = [a for a in self.aristas if (a.origen, a.destino) != e]

    def convierteNoDirigida(self, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                a.dirigida = False

    def invierteDireccion(self, e):
        for a in self.aristas:
            if (a.origen, a.destino) == e and a.dirigida:
                a.origen, a.destino = a.destino, a.origen

    def asignaDireccionDesde(self, e, v):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                a.dirigida = True
                a.origen = v

    def asignaDireccionA(self, e, v):
        for a in self.aristas:
            if (a.origen, a.destino) == e:
                a.dirigida = True
                a.destino = v

    # ================================
    #   VISUALIZACIÓN DEL GRAFO (MEJORADA)
    # ================================
    def mostrarGrafo(self):
        if not self.vertices:
            print("❌ El grafo está vacío.")
            return

        G = nx.DiGraph()
        for v in self.vertices:
            G.add_node(v)
        for a in self.aristas:
            G.add_edge(a.origen, a.destino)

        pos = nx.spring_layout(G, seed=42)
        plt.figure(figsize=(8, 6))
        nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=900, edgecolors='black')
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='-|>', arrowsize=20, edge_color='gray')
        plt.title("🌐 Representación del Grafo", fontsize=14, fontweight='bold')
        plt.axis('off')
        plt.show()


# ================================
#   MENÚ PRINCIPAL (TU VERSIÓN)
# ================================
def menu():
    grafo = Grafo()

    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Insertar vértice")
        print("2. Insertar arista no dirigida")
        print("3. Insertar arista dirigida")
        print("4. Eliminar vértice")
        print("5. Eliminar arista")
        print("6. Mostrar grafo")
        print("7. Mostrar información general")
        print("0. Salir")
        print("====================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            v = input("Nombre del vértice: ")
            grafo.insertaVertice(v)
            print("✔ Vértice agregado correctamente.")

        elif opcion == "2":
            v1 = input("Vértice origen: ")
            v2 = input("Vértice destino: ")
            grafo.insertaArista(v1, v2)
            print("✔ Arista no dirigida agregada.")

        elif opcion == "3":
            v1 = input("Vértice origen: ")
            v2 = input("Vértice destino: ")
            grafo.insertaAristaDirigida(v1, v2)
            print("✔ Arista dirigida agregada.")

        elif opcion == "4":
            v = input("Vértice a eliminar: ")
            grafo.eliminaVertice(v)
            print("✔ Vértice eliminado correctamente.")

        elif opcion == "5":
            v1 = input("Vértice origen: ")
            v2 = input("Vértice destino: ")
            grafo.eliminaArista((v1, v2))
            print("✔ Arista eliminada correctamente.")

        elif opcion == "6":
            grafo.mostrarGrafo()

        elif opcion == "7":
            print(f"Número de vértices: {grafo.numVertices()}")
            print(f"Número de aristas: {grafo.numAristas()}")
            print(f"Vértices: {grafo.vertices}")
            print(f"Aristas: {[ (a.origen, a.destino, 'Dirigida' if a.dirigida else 'No Dirigida') for a in grafo.aristas ]}")

        elif opcion == "0":
            print("👋 Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida, intenta nuevamente.")


# ================================
#   EJECUCIÓN PRINCIPAL
# ================================
if __name__ == "__main__":
    menu()


