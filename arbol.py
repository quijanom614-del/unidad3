class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

class ArbolBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave):
        def _insertar(nodo, clave):
            if nodo is None:
                return Nodo(clave)
            if clave < nodo.clave:
                nodo.izq = _insertar(nodo.izq, clave)
            elif clave > nodo.clave:
                nodo.der = _insertar(nodo.der, clave)
            return nodo
        self.raiz = _insertar(self.raiz, clave)

    def mostrar_acostado(self):
        def _mostrar(nodo, nivel=0):
            if nodo is None:
                return
            _mostrar(nodo.der, nivel + 1)
            print('    ' * nivel + str(nodo.clave))
            _mostrar(nodo.izq, nivel + 1)
        _mostrar(self.raiz)

    def generar_dot(self, filename='arbol.dot'):
        lines = ['digraph BST {', '  node [fontname="Arial"];']
        if self.raiz is None:
            lines.append('  null [label="(vacio)"];')
        else:
            def _node_id(n):
                return f'n{str(id(n))}'
            def _rec(n):
                if n is None:
                    return
                nid = _node_id(n)
                lines.append(f'  {nid} [label="{n.clave}"];')
                if n.izq:
                    lines.append(f'  {nid} -> {_node_id(n.izq)};')
                    _rec(n.izq)
                if n.der:
                    lines.append(f'  {nid} -> {_node_id(n.der)};')
                    _rec(n.der)
            _rec(self.raiz)
        lines.append('}')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        return filename

    def buscar(self, clave):
        def _buscar(nodo, clave):
            if nodo is None:
                return None
            if clave == nodo.clave:
                return nodo
            if clave < nodo.clave:
                return _buscar(nodo.izq, clave)
            else:
                return _buscar(nodo.der, clave)
        return _buscar(self.raiz, clave) is not None

    def preorden(self):
        res = []
        def _pre(n):
            if n:
                res.append(n.clave)
                _pre(n.izq)
                _pre(n.der)
        _pre(self.raiz)
        return res

    def inorden(self):
        res = []
        def _in(n):
            if n:
                _in(n.izq)
                res.append(n.clave)
                _in(n.der)
        _in(self.raiz)
        return res

    def postorden(self):
        res = []
        def _post(n):
            if n:
                _post(n.izq)
                _post(n.der)
                res.append(n.clave)
        _post(self.raiz)
        return res

    def _max_nodo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    def _min_nodo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _delete(self, nodo, clave, estrategia='predecesor'):
        if nodo is None:
            return None
        if clave < nodo.clave:
            nodo.izq = self._delete(nodo.izq, clave, estrategia)
        elif clave > nodo.clave:
            nodo.der = self._delete(nodo.der, clave, estrategia)
        else:
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            if estrategia == 'predecesor':
                pred = self._max_nodo(nodo.izq)
                nodo.clave = pred.clave
                nodo.izq = self._delete(nodo.izq, pred.clave, estrategia)
            else:
                succ = self._min_nodo(nodo.der)
                nodo.clave = succ.clave
                nodo.der = self._delete(nodo.der, succ.clave, estrategia)
        return nodo

    def eliminar_predecesor(self, clave):
        self.raiz = self._delete(self.raiz, clave, 'predecesor')

    def eliminar_sucesor(self, clave):
        self.raiz = self._delete(self.raiz, clave, 'sucesor')

    def por_niveles(self):
        from collections import deque
        res = []
        if self.raiz is None:
            return res
        q = deque([self.raiz])
        while q:
            n = q.popleft()
            res.append(n.clave)
            if n.izq:
                q.append(n.izq)
            if n.der:
                q.append(n.der)
        return res

    def altura(self):
        def _h(n):
            if n is None:
                return -1
            return 1 + max(_h(n.izq), _h(n.der))
        return _h(self.raiz)

    def contar_hojas(self):
        def _c(n):
            if n is None:
                return 0
            if n.izq is None and n.der is None:
                return 1
            return _c(n.izq) + _c(n.der)
        return _c(self.raiz)

    def contar_nodos(self):
        def _c(n):
            if n is None:
                return 0
            return 1 + _c(n.izq) + _c(n.der)
        return _c(self.raiz)

    def es_completo(self):
        from collections import deque
        if self.raiz is None:
            return True
        q = deque([self.raiz])
        encontro_nulo = False
        while q:
            n = q.popleft()
            if n is None:
                encontro_nulo = True
            else:
                if encontro_nulo:
                    return False
                q.append(n.izq)
                q.append(n.der)
        return True

    def es_lleno(self):
        def _lleno(n):
            if n is None:
                return True
            if (n.izq is None) != (n.der is None):
                return False
            return _lleno(n.izq) and _lleno(n.der)
        return _lleno(self.raiz)

    def eliminar_arbol(self):
        self.raiz = None


def menu():
    arbol = ArbolBusqueda()

    while True:
        print("\n--- MENÚ ÁRBOL DE BÚSQUEDA BINARIO ---")
        print("[1] Insertar elemento")
        print("[2] Mostrar árbol completo acostado")
        print("[3] Graficar árbol completo (archivo DOT)")
        print("[4] Buscar un elemento")
        print("[5] Recorrer PreOrden")
        print("[6] Recorrer InOrden")
        print("[7] Recorrer PostOrden")
        print("[8] Eliminar nodo (predecesor)")
        print("[9] Eliminar nodo (sucesor)")
        print("[10] Recorrer por niveles")
        print("[11] Altura del árbol")
        print("[12] Cantidad de hojas")
        print("[13] Cantidad de nodos")
        print("[15] Árbol binario completo?")
        print("[16] Árbol binario lleno?")
        print("[17] Eliminar todo el árbol")
        print("[0] Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            clave = int(input("Ingrese el valor a insertar: "))
            arbol.insertar(clave)
            print("Elemento insertado.")

        elif opcion == '2':
            print("\nÁrbol acostado:")
            arbol.mostrar_acostado()

        elif opcion == '3':
            nombre = input("Nombre del archivo DOT (sin extensión): ") or 'arbol'
            archivo = arbol.generar_dot(nombre + '.dot')
            print(f"Archivo generado: {archivo}")

        elif opcion == '4':
            clave = int(input("Ingrese el valor a buscar: "))
            print("Encontrado" if arbol.buscar(clave) else "No encontrado")

        elif opcion == '5':
            print("PreOrden:", arbol.preorden())

        elif opcion == '6':
            print("InOrden:", arbol.inorden())

        elif opcion == '7':
            print("PostOrden:", arbol.postorden())

        elif opcion == '8':
            clave = int(input("Ingrese el valor a eliminar (predecesor): "))
            arbol.eliminar_predecesor(clave)
            print("Nodo eliminado.")

        elif opcion == '9':
            clave = int(input("Ingrese el valor a eliminar (sucesor): "))
            arbol.eliminar_sucesor(clave)
            print("Nodo eliminado.")

        elif opcion == '10':
            print("Recorrido por niveles:", arbol.por_niveles())

        elif opcion == '11':
            print("Altura del árbol:", arbol.altura())

        elif opcion == '12':
            print("Cantidad de hojas:", arbol.contar_hojas())

        elif opcion == '13':
            print("Cantidad de nodos:", arbol.contar_nodos())

        elif opcion == '15':
            print("¿Es completo?:", arbol.es_completo())

        elif opcion == '16':
            print("¿Es lleno?:", arbol.es_lleno())

        elif opcion == '17':
            arbol.eliminar_arbol()
            print("Árbol eliminado.")

        elif opcion == '0':
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")

if __name__ == '__main__':
    menu()
