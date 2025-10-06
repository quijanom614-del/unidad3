# Definición de la clase Cola
class Cola:
    def __init__(self):
        self.items = []  # Lista donde se guardan los elementos de la cola

    def esta_vacia(self):
        return len(self.items) == 0  # Verifica si la cola está vacía

    def encolar(self, elemento):
        self.items.append(elemento)  # Agrega un elemento al final de la cola

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)  # Quita y devuelve el primer elemento
        else:
            return None  # Si está vacía, retorna None

    def mostrar(self):
        return self.items  # Retorna todos los elementos de la cola

# Función que recibe dos colas y devuelve una cola con la suma de sus elementos
def sumar_colas(colaA, colaB):
    cola_resultado = Cola()

    while not colaA.esta_vacia() and not colaB.esta_vacia():
        a = colaA.desencolar()
        b = colaB.desencolar()
        cola_resultado.encolar(a + b)

    return cola_resultado

# Programa principal
print("=== SUMA DE DOS COLAS ===")

# Crear las dos colas
colaA = Cola()
colaB = Cola()

# Ingreso de datos por el usuario
n = int(input("¿Cuántos elementos tendrá cada cola? "))

print("\n--- Ingrese los valores para la Cola A ---")
for i in range(n):
    valor = int(input(f"Ingrese el elemento {i+1}: "))
    colaA.encolar(valor)

print("\n--- Ingrese los valores para la Cola B ---")
for i in range(n):
    valor = int(input(f"Ingrese el elemento {i+1}: "))
    colaB.encolar(valor)

# Mostrar las colas originales
print("\nCola A:", colaA.mostrar())
print("Cola B:", colaB.mostrar())

# Sumar las colas
resultado = sumar_colas(colaA, colaB)

# Mostrar el resultado final
print("\nCola Resultado (suma de A y B):", resultado.mostrar())


