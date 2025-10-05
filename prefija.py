class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def mostrar(self):
        return self.items



def prioridad(op):
    if op in ["+", "-"]:
        return 1
    if op in ["*", "/"]:
        return 2
    return 0

def infija_a_posfija(tokens):
    salida = []
    pila = Pila()
    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token == "(":
            pila.apilar(token)
        elif token == ")":
            while pila.ver_tope() != "(":
                salida.append(pila.desapilar())
            pila.desapilar()
        else:  # operador
            while (not pila.esta_vacia() and
                   prioridad(pila.ver_tope()) >= prioridad(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)
    while not pila.esta_vacia():
        salida.append(pila.desapilar())
    return salida

def infija_a_prefija(tokens):
    tokens = tokens[::-1]
    for i in range(len(tokens)):
        if tokens[i] == "(":
            tokens[i] = ")"
        elif tokens[i] == ")":
            tokens[i] = "("
    posfija = infija_a_posfija(tokens)
    return posfija[::-1]


if __name__ == "__main__":
    
    expresion = input("Ingrese la expresión en notación infija (ejemplo: 3 + 4 * ( 2 - 1 )):\n> ")

    
    tokens = expresion.split()
    pila = Pila()
    for token in tokens:
        pila.apilar(token)

    print("\nContenido de la pila (tokens en orden):", pila.mostrar())

 
    opcion = input("\n¿Cómo quieres ver la expresión? (infija / posfija / prefija): ").lower()

    if opcion == "infija":
        print("Expresión infija:", " ".join(tokens))
    elif opcion == "posfija":
        posfija = infija_a_posfija(tokens)
        print("Expresión posfija:", " ".join(posfija))
    elif opcion == "prefija":
        prefija = infija_a_prefija(tokens)
        print("Expresión prefija:", " ".join(prefija))
    else:
        print("Opción no válida.")

