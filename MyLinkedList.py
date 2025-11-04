
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None



class MyLinkedList:
    def __init__(self):
        self.cabeza = None

    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

   
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print(" → ".join(map(str, elementos)) if elementos else "(lista vacía)")

   
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                return True
            actual = actual.siguiente
        return False

    
    def eliminar(self, valor):
        if self.cabeza is None:
            print("La lista está vacía.")
            return

       
        if self.cabeza.dato == valor:
            self.cabeza = self.cabeza.siguiente
            return

        
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != valor:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
        else:
            print("Elemento no encontrado.")

    def insertar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

 
    def tamano(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    
    def vaciar(self):
        self.cabeza = None
