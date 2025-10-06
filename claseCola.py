
class Cola:
    def __init__(self):
        self.items = []  

    def esta_vacia(self):
        return len(self.items) == 0  

    def encolar(self, elemento):
        self.items.append(elemento)  

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)  
        else:
            return None  

    def mostrar(self):
        return self.items  


def sumar_colas(colaA, colaB):
    cola_resultado = Cola()

    while not colaA.esta_vacia() and not colaB.esta_vacia():
        a = colaA.desencolar()
        b = colaB.desencolar()
        cola_resultado.encolar(a + b)

    return cola_resultado


print("=== SUMA DE DOS COLAS ===")


colaA = Cola()
colaB = Cola()

n = int(input("¿Cuántos elementos tendrá cada cola? "))

print("\n--- Ingrese los valores para la Cola A ---")
for i in range(n):
    valor = int(input(f"Ingrese el elemento {i+1}: "))
    colaA.encolar(valor)

print("\n--- Ingrese los valores para la Cola B ---")
for i in range(n):
    valor = int(input(f"Ingrese el elemento {i+1}: "))
    colaB.encolar(valor)


print("\nCola A:", colaA.mostrar())
print("Cola B:", colaB.mostrar())

resultado = sumar_colas(colaA, colaB)


print("\nCola Resultado (suma de A y B):", resultado.mostrar())


