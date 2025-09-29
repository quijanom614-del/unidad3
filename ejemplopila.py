import tkinter as tk
from tkinter import messagebox

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def esta_vacia(self):
        return len(self.items) == 0

class VentanaPila:
    def __init__(self, root):
        self.root = root
        self.root.title("Pila con interfaz gráfica")
        self.pila = Pila()

        # Entrada para valores
        self.entry = tk.Entry(root, width=20)
        self.entry.pack(pady=5)

        # Botones
        tk.Button(root, text="Apilar", command=self.apilar).pack(pady=2)
        tk.Button(root, text="Desapilar", command=self.desapilar).pack(pady=2)
        tk.Button(root, text="Ver cima", command=self.ver_cima).pack(pady=2)

        # Canvas para mostrar pila
        self.canvas = tk.Canvas(root, width=200, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.actualizar_pila()

    def apilar(self):
        valor = self.entry.get()
        if valor:
            self.pila.apilar(valor)
            self.entry.delete(0, tk.END)
            self.actualizar_pila()
        else:
            messagebox.showwarning("Aviso", "Ingresa un valor para apilar")

    def desapilar(self):
        eliminado = self.pila.desapilar()
        if eliminado is not None:
            messagebox.showinfo("Desapilado", f"Se quitó: {eliminado}")
        else:
            messagebox.showwarning("Aviso", "La pila está vacía")
        self.actualizar_pila()

    def ver_cima(self):
        cima = self.pila.cima()
        if cima is not None:
            messagebox.showinfo("Cima", f"Elemento en la cima: {cima}")
        else:
            messagebox.showwarning("Aviso", "La pila está vacía")

    def actualizar_pila(self):
        self.canvas.delete("all")
        x1, y1 = 50, 250  # posición inicial
        for elemento in reversed(self.pila.items):  # mostrar de abajo hacia arriba
            self.canvas.create_rectangle(x1, y1, x1+100, y1-40, fill="lightblue")
            self.canvas.create_text(x1+50, y1-20, text=str(elemento))
            y1 -= 45

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPila(root)
    root.mainloop()
