from bisect import bisect_left

class PostresManager:
    def __init__(self):
        self.postres = []  

    def _key(self, name: str):
        return name.strip().lower()

    def _find_index(self, name: str):
        key = self._key(name)
        for i, (postre, _) in enumerate(self.postres):
            if self._key(postre) == key:
                return i
        return None

    def _insert_sorted(self, name: str, ingredients: list):
        key = self._key(name)
        keys = [self._key(p[0]) for p in self.postres]
        pos = bisect_left(keys, key)
        if pos < len(self.postres) and keys[pos] == key:
            return False
        self.postres.insert(pos, (name, ingredients))
        return True

    
    def mostrar_ingredientes(self, name: str):
        idx = self._find_index(name)
        if idx is None:
            print(f"❌ El postre '{name}' no existe.")
            return
        print(f"🍮 Ingredientes de '{name}':")
        for ing in self.postres[idx][1]:
            print(f"  - {ing}")

  
    def agregar_ingredientes(self, name: str):
        idx = self._find_index(name)
        if idx is None:
            print(f"❌ El postre '{name}' no existe.")
            return
        nuevos = input("👉 Ingresa los nuevos ingredientes separados por coma: ").split(",")
        nuevos = [n.strip() for n in nuevos if n.strip()]
        actuales = self.postres[idx][1]
        for ing in nuevos:
            if ing not in actuales:
                actuales.append(ing)
        print(f"✅ Ingredientes agregados a '{name}' correctamente.")

    
    def eliminar_ingrediente(self, name: str):
        idx = self._find_index(name)
        if idx is None:
            print(f"❌ El postre '{name}' no existe.")
            return
        ingrediente = input("🍓 Ingresa el ingrediente a eliminar: ").strip()
        if ingrediente in self.postres[idx][1]:
            self.postres[idx][1].remove(ingrediente)
            print(f"✅ Ingrediente '{ingrediente}' eliminado de '{name}'.")
        else:
            print(f"⚠️ El ingrediente '{ingrediente}' no existe en '{name}'.")

   
    def alta_postre(self):
        name = input("🍰 Ingresa el nombre del nuevo postre: ").strip()
        ingredientes = input("🧂 Ingresa los ingredientes separados por coma: ").split(",")
        ingredientes = [i.strip() for i in ingredientes if i.strip()]
        if self._insert_sorted(name, ingredientes):
            print(f"✅ Postre '{name}' agregado correctamente.")
        else:
            print(f"⚠️ El postre '{name}' ya existe.")

    
    def baja_postre(self):
        name = input("🗑️ Ingresa el nombre del postre a eliminar: ").strip()
        idx = self._find_index(name)
        if idx is not None:
            del self.postres[idx]
            print(f"✅ Postre '{name}' eliminado con éxito.")
        else:
            print(f"❌ El postre '{name}' no existe.")

   
    def eliminar_duplicados(self):
        vistos = {}
        nuevos = []
        for name, ingredientes in self.postres:
            key = self._key(name)
            if key not in vistos:
                vistos[key] = set(ingredientes)
                nuevos.append((name, ingredientes))
            else:
               
                vistos[key].update(ingredientes)
        self.postres = [(n, list(ings)) for n, ings in nuevos]
        print("♻️ Duplicados eliminados correctamente (listas fusionadas).")

   
    def mostrar_todos(self):
        if not self.postres:
            print("📂 No hay postres registrados.")
            return
        print("\n📖 LISTA DE POSTRES:")
        for name, ingredientes in self.postres:
            print(f"🍨 {name}: {', '.join(ingredientes)}")



def menu():
    gestor = PostresManager()

    while True:
        print("\n===========================")
        print("   MENÚ DE POSTRES 🍧")
        print("===========================")
        print("1. Mostrar ingredientes de un postre")
        print("2. Agregar ingredientes a un postre")
        print("3. Eliminar ingrediente de un postre")
        print("4. Dar de alta un nuevo postre")
        print("5. Dar de baja un postre")
        print("6. Eliminar postres duplicados")
        print("7. Mostrar todos los postres")
        print("0. Salir")
        print("===========================")

        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            nombre = input("🍩 Ingresa el nombre del postre: ")
            gestor.mostrar_ingredientes(nombre)
        elif opcion == "2":
            nombre = input("🍪 Ingresa el nombre del postre: ")
            gestor.agregar_ingredientes(nombre)
        elif opcion == "3":
            nombre = input("🧁 Ingresa el nombre del postre: ")
            gestor.eliminar_ingrediente(nombre)
        elif opcion == "4":
            gestor.alta_postre()
        elif opcion == "5":
            gestor.baja_postre()
        elif opcion == "6":
            gestor.eliminar_duplicados()
        elif opcion == "7":
            gestor.mostrar_todos()
        elif opcion == "0":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu()

