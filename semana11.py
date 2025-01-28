
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def construir_arbol(self, expresion):
        """
        Construye el árbol binario a partir de una expresión Lambda en forma de lista.
        """
        pila = []
        for token in expresion:
            if isinstance(token, (int, float, str)):  # Es un operando
                pila.append(Nodo(token))
            elif callable(token):  # Es un operador o función Lambda
                nodo = Nodo(token)
                nodo.derecho = pila.pop()
                nodo.izquierdo = pila.pop()
                pila.append(nodo)
        self.raiz = pila.pop()

    def evaluar(self, nodo=None):
        """
        Evalúa la expresión representada por el árbol.
        """
        if nodo is None:
            nodo = self.raiz

        if nodo.izquierdo is None and nodo.derecho is None:  # Nodo hoja
            return nodo.valor

        # Evaluación de los subárboles izquierdo y derecho
        izquierdo = self.evaluar(nodo.izquierdo)
        derecho = self.evaluar(nodo.derecho)

        # Aplicación del operador o función Lambda
        return nodo.valor(izquierdo, derecho)

# Ejemplo de uso
if __name__ == "__main__":
    # Definir operadores como funciones Lambda
    suma = lambda x, y: x + y
    resta = lambda x, y: x - y
    multiplicacion = lambda x, y: x * y
    division = lambda x, y: x / y

    # Prueba 1: Evaluar 3 + 5
    expresion1 = [3, 5, suma]  # Representa: 3 + 5
    arbol1 = ArbolBinario()
    arbol1.construir_arbol(expresion1)
    print("Resultado de 3 + 5:", arbol1.evaluar())

    # Prueba 2: Evaluar (2 * 4) - 3
    expresion2 = [2, 4, multiplicacion, 3, resta]  # Representa: (2 * 4) - 3
    arbol2 = ArbolBinario()
    arbol2.construir_arbol(expresion2)
    print("Resultado de (2 * 4) - 3:", arbol2.evaluar())

    # Prueba 3: Evaluar (10 / 2) + (3 * 4)
    expresion3 = [10, 2, division, 3, 4, multiplicacion, suma]  # Representa: (10 / 2) + (3 * 4)
    arbol3 = ArbolBinario()
    arbol3.construir_arbol(expresion3)
    print("Resultado de (10 / 2) + (3 * 4):", arbol3.evaluar())


