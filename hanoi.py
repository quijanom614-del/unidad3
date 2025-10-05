class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def __str__(self):
        return f"{self.nombre}: {self.items}"


# Crear las tres torres
origen = Pila("A (Origen)")
auxiliar = Pila("B (Auxiliar)")
destino = Pila("C (Destino)")

# Inicializar con 3 discos (de mayor a menor)
for disco in range(3, 0, -1):
    origen.apilar(disco)


def mostrar_estado():
    print("\nEstado actual de las torres:")
    print(origen)
    print(auxiliar)
    print(destino)
    print("-" * 35)


def mover_disco(desde, hacia):
    if desde.esta_vacia():
        print("⚠️ No hay discos en esa torre.")
        return False

    disco = desde.ver_tope()
    if not hacia.esta_vacia() and hacia.ver_tope() < disco:
        print("⚠️ Movimiento inválido: no puedes poner un disco grande sobre uno pequeño.")
        return False

    desde.desapilar()
    hacia.apilar(disco)
    print(f"✅ Moviste el disco {disco} de {desde.nombre} a {hacia.nombre}")
    return True


# --- Juego principal ---
print("🎮 TORRES DE HANOI - 3 DISCOS")
print("Objetivo: mover todos los discos de A (Origen) a C (Destino).")
print("Para salir del juego, escribe 'SALIR' en cualquier momento.\n")
mostrar_estado()

while True:
    desde = input("Mover desde torre (A, B o C): ").upper()
    if desde == "SALIR":
        print("👋 Gracias por jugar. ¡Hasta luego!")
        break

    hacia = input("Hacia torre (A, B o C): ").upper()
    if hacia == "SALIR":
        print("👋 Gracias por jugar. ¡Hasta luego!")
        break

    torres = {'A': origen, 'B': auxiliar, 'C': destino}

    if desde in torres and hacia in torres:
        mover_disco(torres[desde], torres[hacia])
    else:
        print("⚠️ Torre no válida. Usa A, B o C, o escribe 'SALIR' para salir.")

    mostrar_estado()

    # Condición de victoria (discos en orden correcto en C)
    if destino.items == [3, 2, 1]:
        print("🎉 ¡Felicidades! Completaste el juego correctamente.")
        break
