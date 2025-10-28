
class Order:
    def __init__(self, cliente, cantidad):
        self.cliente = cliente
        self.cantidad = cantidad

    def __str__(self):
        return f"Pedido de {self.cliente} - Cantidad: {self.cantidad}"



class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None



class ColaPedidos:
    def __init__(self):
        self.frente = None  
        self.fin = None    

  
    def esta_vacia(self):
        return self.frente is None

   
    def agregar_pedido(self, pedido):
        nuevo = Nodo(pedido)
        if self.esta_vacia():
            self.frente = nuevo
            self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            self.fin = nuevo
        print(f"✅ Pedido agregado: {pedido}")

    
    def procesar_pedido(self):
        if self.esta_vacia():
            print("⚠️ No hay pedidos por procesar.")
            return None
        pedido = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.fin = None
        print(f"📦 Pedido procesado: {pedido}")
        return pedido

  
    def ver_siguiente_pedido(self):
        if self.esta_vacia():
            print("ℹ️ No hay pedidos pendientes.")
            return None
        return self.frente.dato

 
    def mostrar_pedidos(self):
        if self.esta_vacia():
            print("No hay pedidos en la cola.")
            return
        actual = self.frente
        print("\n📋 Pedidos en espera:")
        while actual is not None:
            print(" -", actual.dato)
            actual = actual.siguiente

def main():
    cola = ColaPedidos()

    print("=== RECEPCIÓN DE PEDIDOS ===")

    
    while True:
        cliente = input("\nIngrese el nombre del cliente (o 'fin' para terminar): ")
        if cliente.lower() == "fin":
            break
        cantidad = int(input("Ingrese la cantidad de producto: "))
        pedido = Order(cliente, cantidad)
        cola.agregar_pedido(pedido)

    
    cola.mostrar_pedidos()

    
    print("\n=== PROCESAMIENTO DE PEDIDOS ===")
    while not cola.esta_vacia():
        input("Presione ENTER para procesar el siguiente pedido...")
        cola.procesar_pedido()

    print("\n✅ Todos los pedidos han sido procesados.")

if __name__ == "__main__":
    main()
