import random
import time


lista_original = random.sample(range(1, 5000), 1000)


def espera(modo, delay):
    if modo == "manual":
        input("Presiona Enter para ver el siguiente paso...")
    elif modo == "auto":
        time.sleep(delay)

def format_list_view(lst, highlights=None, full_display=False, window=5):
    """
    Devuelve una cadena con una representación legible de la lista.
    - Si full_display True -> muestra toda la lista.
    - Si len(lst) > 60 y full_display False -> muestra:
        primeros 10, ..., ventana alrededor de highlights, ..., últimos 10
      para que se vea dónde ocurren los cambios sin imprimir 1000 números.
    - highlights: iterable de índices a resaltar (se encierran con [ ]).
    """
    n = len(lst)
    highlights = set(highlights or [])
    def show_segment(start, end):
        parts = []
        for i in range(start, end):
            s = str(lst[i])
            if i in highlights:
                s = f"[{s}]"
            parts.append(s)
        return ", ".join(parts)

    if full_display or n <= 60:
        return "[" + ", ".join(("[{}]".format(x) if i in highlights else str(x)) 
                              for i, x in enumerate(lst)) + "]"

    
    left_count = 10
    right_count = 10

    segments = []
    segments.append(show_segment(0, min(left_count, n)))

    
    mid_indices = set()
    for idx in highlights:
        for k in range(idx - window, idx + window + 1):
            if 0 <= k < n:
                mid_indices.add(k)

    
    if not mid_indices:
        mid_start = max(left_count, (n // 2) - window)
        mid_end = min(n - right_count, mid_start + 2*window + 1)
        if mid_start < mid_end:
            segments.append("...")
            segments.append(show_segment(mid_start, mid_end))
            segments.append("...")
    else:
        
        mids = sorted(mid_indices)
        
        mids = [m for m in mids if m >= left_count and m < n - right_count]
        if mids:
            runs = []
            run = [mids[0], mids[0]]
            for x in mids[1:]:
                if x <= run[1] + 1:
                    run[1] = x
                else:
                    runs.append(tuple(run))
                    run = [x, x]
            runs.append(tuple(run))
            for (s, e) in runs:
                segments.append("...")
                segments.append(show_segment(s, e+1))
            segments.append("...")
        else:
            segments.append("...")

    
    if n > right_count:
        segments.append(show_segment(n - right_count, n))
    return "[" + " , ".join(segments) + "]"


def burbuja(lista, show_steps=False, modo="manual", delay=0.1, full_display=False):
    lst = lista[:]
    n = len(lst)
    pasos = 0

    if show_steps:
        print("\n=== BURBUJA: inicio ===")
        print("Estado inicial:", format_list_view(lst, full_display=full_display))

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            pasos += 1  
            if show_steps:
                print(f"\n[Burbuja] Comparando índices {j} y {j+1}: {lst[j]} ? {lst[j+1]}")
                espera(modo, delay)

            if lst[j] > lst[j + 1]:
               
                a, b = lst[j], lst[j+1]
                lst[j], lst[j + 1] = b, a
                pasos += 1  
                swapped = True
                if show_steps:
                    print(f" → Swap: intercambiando {a} y {b} (índices {j}, {j+1})")
                    print("   Estado ahora:", format_list_view(lst, highlights=(j, j+1), full_display=full_display))
                    espera(modo, delay)
        if not swapped:
            if show_steps:
                print("\nNo hubo swaps en esta pasada; lista ya ordenada.")
            break

    if show_steps:
        print("\n=== BURBUJA: final ===")
        print("Resultado:", format_list_view(lst, full_display=full_display))

    return lst, pasos

def insercion(lista, show_steps=False, modo="manual", delay=0.1, full_display=False):
    lst = lista[:]
    pasos = 0
    if show_steps:
        print("\n=== INSERCIÓN: inicio ===")
        print("Estado inicial:", format_list_view(lst, full_display=full_display))

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        if show_steps:
            print(f"\n[Inserción] Tomamos clave = {key} (índice {i}). Parte izquierda 0..{i-1} está ordenada.")
            espera(modo, delay)

        
        moved = False
        while j >= 0 and lst[j] > key:
            if show_steps:
                print(f" → {lst[j]} (índice {j}) > {key} -> mover {lst[j]} a la posición {j+1}")
            lst[j + 1] = lst[j]
            pasos += 1  
            moved = True
            if show_steps:
                print("   Estado intermedio:", format_list_view(lst, highlights=(j, j+1), full_display=full_display))
                espera(modo, delay)
            j -= 1
        lst[j + 1] = key
        pasos += 1  
        if show_steps:
            if moved:
                print(f" → Insertar {key} en posición {j+1}")
            else:
                print(f" → {key} ya está en la posición correcta ({j+1})")
            print("   Estado ahora:", format_list_view(lst, highlights=(j+1,), full_display=full_display))
            espera(modo, delay)

    if show_steps:
        print("\n=== INSERCIÓN: final ===")
        print("Resultado:", format_list_view(lst, full_display=full_display))

    return lst, pasos

def seleccion(lista, show_steps=False, modo="manual", delay=0.1, full_display=False):
    lst = lista[:]
    n = len(lst)
    pasos = 0

    if show_steps:
        print("\n=== SELECCIÓN: inicio ===")
        print("Estado inicial:", format_list_view(lst, full_display=full_display))

    for i in range(n):
        minimo = i
        if show_steps:
            print(f"\n[Selección] Buscando el mínimo en la sublista desde índice {i} hasta {n-1}")
            espera(modo, delay)

        for j in range(i + 1, n):
            pasos += 1 
            if show_steps:
                print(f" → Comparando {lst[j]} (índice {j}) con mínimo actual {lst[minimo]} (índice {minimo})")
                espera(modo, delay)
            if lst[j] < lst[minimo]:
                minimo = j
                if show_steps:
                    print(f"   Nuevo mínimo: {lst[minimo]} en índice {minimo}")
                    print("   Estado (resaltado mínimo):", format_list_view(lst, highlights=(minimo,), full_display=full_display))
                    espera(modo, delay)

        if minimo != i:
            a, b = lst[i], lst[minimo]
            lst[i], lst[minimo] = b, a
            pasos += 1  
            if show_steps:
                print(f" → Swap: colocar mínimo {lst[i]} en la posición {i} (intercambio {a}↔{b})")
                print("   Estado ahora:", format_list_view(lst, highlights=(i, minimo), full_display=full_display))
                espera(modo, delay)
        else:
            if show_steps:
                print(f" → El elemento en posición {i} ya es el mínimo; no se hace swap.")
                espera(modo, delay)

    if show_steps:
        print("\n=== SELECCIÓN: final ===")
        print("Resultado:", format_list_view(lst, full_display=full_display))

    return lst, pasos


def menu():
    global lista_original
    modo = "manual"
    delay = 0.1
    full_display = False

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver parte de la lista generada")
        print("2. Ordenar por Burbuja (paso a paso)")
        print("3. Ordenar por Inserción (paso a paso)")
        print("4. Ordenar por Selección (paso a paso)")
        print("5. Cambiar modo paso a paso (actual: {})".format(modo))
        print("6. Alternar vista completa (actual: {})".format("SI" if full_display else "NO"))
        print("7. Regenerar lista de 1000 números")
        print("8. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            print("Lista (primeros 60 elementos):")
            print(format_list_view(lista_original, full_display=False))

        elif opcion == "2":
            pasos_flag = input("¿Mostrar paso a paso? (s/n): ").strip().lower() == 's'
            if not pasos_flag:
               
                resultado, total_pasos = burbuja(lista_original, show_steps=False)
                print("Resultado (Burbuja):", format_list_view(resultado, full_display=True))
                print("Total de pasos realizados:", total_pasos)
            else:
                resultado, total_pasos = burbuja(lista_original, show_steps=True, modo=modo, delay=delay, full_display=full_display)
                print("Total de pasos realizados:", total_pasos)

        elif opcion == "3":
            pasos_flag = input("¿Mostrar paso a paso? (s/n): ").strip().lower() == 's'
            if not pasos_flag:
                resultado, total_pasos = insercion(lista_original, show_steps=False)
                print("Resultado (Inserción):", format_list_view(resultado, full_display=True))
                print("Total de pasos realizados:", total_pasos)
            else:
                resultado, total_pasos = insercion(lista_original, show_steps=True, modo=modo, delay=delay, full_display=full_display)
                print("Total de pasos realizados:", total_pasos)

        elif opcion == "4":
            pasos_flag = input("¿Mostrar paso a paso? (s/n): ").strip().lower() == 's'
            if not pasos_flag:
                resultado, total_pasos = seleccion(lista_original, show_steps=False)
                print("Resultado (Selección):", format_list_view(resultado, full_display=True))
                print("Total de pasos realizados:", total_pasos)
            else:
                resultado, total_pasos = seleccion(lista_original, show_steps=True, modo=modo, delay=delay, full_display=full_display)
                print("Total de pasos realizados:", total_pasos)

        elif opcion == "5":
            modo_in = input("Elige modo ('manual' o 'auto'): ").strip().lower()
            if modo_in in ("manual", "auto"):
                modo = modo_in
                if modo == "auto":
                    try:
                        delay = float(input("Delay entre pasos (ej: 0.1): ").strip() or "0.1")
                    except ValueError:
                        delay = 0.1
                print("Modo actualizado a", modo, "con delay", delay)
            else:
                print("Modo inválido. Manteniendo:", modo)

        elif opcion == "6":
            full_display = not full_display
            print("Vista completa ahora:", "SI" if full_display else "NO (vista compacta)")

        elif opcion == "7":
            lista_original = random.sample(range(1, 5000), 1000)
            print("Nueva lista generada.")

        elif opcion == "8":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()


