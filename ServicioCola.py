# Clase Cola
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


# Clase principal del sistema de atención
class SistemaSeguros:
    def __init__(self, num_servicios):
        self.colas = [Cola() for _ in range(num_servicios)]  # Lista de colas
        self.contadores = [1 for _ in range(num_servicios)]  # Contadores de turnos

    def llegada_cliente(self, servicio):
        numero_turno = f"S{servicio}-{self.contadores[servicio - 1]}"
        self.colas[servicio - 1].encolar(numero_turno)
        self.contadores[servicio - 1] += 1
        print(f"Cliente agregado a servicio {servicio}. Turno: {numero_turno}")

    def atender_cliente(self, servicio):
        if self.colas[servicio - 1].esta_vacia():
            print(f"No hay clientes en la cola del servicio {servicio}.")
        else:
            turno = self.colas[servicio - 1].desencolar()
            print(f"Atendiendo al cliente con turno: {turno}")

    def mostrar_colas(self):
        print("\nEstado actual de las colas:")
        for i, cola in enumerate(self.colas, start=1):
            print(f"Servicio {i}: {cola.mostrar()}")


# Programa principal
def main():
    print("=== SISTEMA DE COLAS - COMPAÑÍA DE SEGUROS ===")
    num_servicios = int(input("Ingrese el número de servicios disponibles: "))
    sistema = SistemaSeguros(num_servicios)

    print("\nComandos disponibles:")
    print("C# -> Cliente llega (ejemplo: C1 para servicio 1)")
    print("A# -> Atender cliente (ejemplo: A1 para servicio 1)")
    print("M  -> Mostrar estado de las colas")
    print("S  -> Salir del sistema")

    while True:
        comando = input("\nIngrese un comando: ").strip().upper()

        if comando == "S":
            print("Saliendo del sistema...")
            break

        elif comando == "M":
            sistema.mostrar_colas()

        elif comando.startswith("C"):
            try:
                servicio = int(comando[1:])
                sistema.llegada_cliente(servicio)
            except:
                print("Comando inválido. Ejemplo correcto: C1")

        elif comando.startswith("A"):
            try:
                servicio = int(comando[1:])
                sistema.atender_cliente(servicio)
            except:
                print("Comando inválido. Ejemplo correcto: A1")

        else:
            print("Comando no reconocido. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()

