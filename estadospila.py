class Pila:
    def __init__(self, capacidad):
        self.items = []
        self.capacidad = capacidad

    def esta_llena(self):
        return len(self.items) == self.capacidad

    def esta_vacia(self):
        return len(self.items) == 0

    def insertar(self, elemento):
        if not self.esta_llena():
            self.items.append(elemento)
            print(f"Insertar({elemento}) realizado con éxito.")
        else:
            print("❌ La pila está llena. No se puede insertar más elementos.")
        self.mostrar()

    def eliminar(self, nombre_operacion):
        if not self.esta_vacia():
            eliminado = self.items.pop()
            print(f"Eliminar({nombre_operacion}) -> Se quitó '{eliminado}' del tope.")
        else:
            print(f"Eliminar({nombre_operacion}) -> ❌ La pila está vacía. No se puede eliminar.")
        self.mostrar()

    def mostrar(self):
        print("\nEstado actual de la pila:")
        if self.esta_vacia():
            print("[ Vacía ]")
        else:
            for i in range(len(self.items)-1, -1, -1):
                print(f"| {self.items[i]} |")
        print(f"TOPE = {len(self.items)}\n{'-'*25}")


# Programa principal
pila = Pila(8)

# Operaciones dadas
pila.insertar("X")  # a
pila.insertar("Y")  # b
pila.eliminar("Z")  # c
pila.eliminar("T")  # d
pila.eliminar("U")  # e
pila.insertar("V")  # f
pila.insertar("W")  # g
pila.eliminar("p")  # h
pila.insertar("R")  # i
