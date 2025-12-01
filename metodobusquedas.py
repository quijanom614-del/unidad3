import sys



def busqueda_secuencial(data_list, valor_buscado):
    """Búsqueda Secuencial: Itera sobre una lista desordenada."""
   
    valor_buscado = str(valor_buscado)
    
    for indice, elemento in enumerate(data_list):
        if elemento == valor_buscado:
            return indice
    return -1

def busqueda_binaria(data_list_sorted, valor_buscado):
    """Búsqueda Binaria: Divide y vencerás en una lista ordenada."""
    
    try:
        valor_buscado = int(valor_buscado)
    except ValueError:
        return -2 

    inicio = 0
    fin = len(data_list_sorted) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        
        if data_list_sorted[medio] == valor_buscado:
            return medio
        elif data_list_sorted[medio] < valor_buscado:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def busqueda_hash(data_dict, clave_buscada):
    """Búsqueda Hash: Acceso directo por clave en un diccionario."""
    
    if clave_buscada in data_dict:
        return data_dict[clave_buscada] 
    return None



def convertir_a_hash(data_list_numerica):
    """Convierte una lista numérica a un diccionario (Hash) usando el índice como clave."""
    hash_map = {}
    for indice, valor in enumerate(data_list_numerica):
        
        hash_map[str(indice)] = valor 
    return hash_map

def obtener_datos_iniciales():
    """Solicita al usuario una lista de números para trabajar."""
    while True:
        try:
            print("\n--- 📝 Configuración de Datos Base ---")
            entrada = input("Ingrese la lista de NÚMEROS (separados por coma, ej: 10,50,30,80): ")
            data_list_numerica = [int(item.strip()) for item in entrada.split(',')]
            
            if not data_list_numerica:
                print("❌ La lista no puede estar vacía. Intente de nuevo.")
                continue
            
            return data_list_numerica
        except ValueError:
            print("❌ Error: Por favor, ingrese solo números enteros.")

def main():
    
    
    datos_base = obtener_datos_iniciales()
    
    
    lista_original_str = [str(x) for x in datos_base] # Para Secuencial (cadenas)
    lista_ordenada_num = sorted(datos_base) # Para Binaria (ordenada y numérica)
    tabla_hash = convertir_a_hash(datos_base) # Para Hash (índice:valor)
    
    print(f"\n✅ Datos Base para Búsqueda: {datos_base}")
    print(f"   -> Secuencial usará: {lista_original_str}")
    print(f"   -> Binaria usará: {lista_ordenada_num}")
    print(f"   -> Hash usará claves (índices): {list(tabla_hash.keys())}")

    while True:
        print("\n--- 🔍 Seleccione el Método de Búsqueda ---")
        print("1. Búsqueda Secuencial (Lista original)")
        print("2. Búsqueda Binaria (Lista ordenada)")
        print("3. Búsqueda Hash (Diccionario por índice)")
        print("4. Ingresar nuevos datos")
        print("5. Salir")
        print("------------------------------------------")
        
        opcion = input("👉 Opción (1-5): ")

        if opcion == '5':
            print("¡Adiós! 👋")
            sys.exit()
        elif opcion == '4':
            main() 
            return
            
        if opcion in ('1', '2', '3'):
            valor_buscado = input("🎯 Ingrese el valor a buscar: ")
        else:
            print("Opción no válida.")
            continue
            
       
        
        if opcion == '1':
            resultado = busqueda_secuencial(lista_original_str, valor_buscado)
            if resultado != -1:
                print(f"\n✅ SECUENCIAL: '{valor_buscado}' encontrado en el índice {resultado}.")
            else:
                print(f"\n❌ SECUENCIAL: '{valor_buscado}' no encontrado.")
            
        elif opcion == '2':
            resultado = busqueda_binaria(lista_ordenada_num, valor_buscado)
            if resultado == -2:
                 print("\n❌ BINARIA: El valor de búsqueda debe ser numérico.")
            elif resultado != -1:
                print(f"\n✅ BINARIA: '{valor_buscado}' encontrado en el índice {resultado}.")
            else:
                print(f"\n❌ BINARIA: '{valor_buscado}' no encontrado.")
            
        elif opcion == '3':
            
            print(f"🚨 Para la Búsqueda Hash, el valor de búsqueda se interpreta como la CLAVE (índice 0, 1, 2, etc.)")
            clave_buscada = valor_buscado
            
            resultado = busqueda_hash(tabla_hash, clave_buscada)
            
            if resultado is not None:
                print(f"\n✅ HASH: La CLAVE '{clave_buscada}' encontró el VALOR: '{resultado}'.")
            else:
                print(f"\n❌ HASH: Clave '{clave_buscada}' no encontrada.")
            
if __name__ == "__main__":
    main()