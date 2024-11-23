# pila.py
class Pila:
    def __init__(self):
        """Inicializa una pila vacía"""
        self.items = []

    def push(self, item):
        """Agrega un elemento a la pila"""
        self.items.append(item)

    def pop(self):
        """Elimina y retorna el elemento superior de la pila"""
        if not self.esta_vacia():
            return self.items.pop()
        raise IndexError("La pila está vacía")

    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        return len(self.items) == 0

    def peek(self):
        """Muestra el elemento superior de la pila sin eliminarlo"""
        if not self.esta_vacia():
            return self.items[-1]
        raise IndexError("La pila está vacía")
