class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self, expresion):
        self.raiz = self.construir_arbol(expresion)

    def construir_arbol(self, expresion):
        pila = []
        for simbolo in expresion:
            if simbolo.isdigit():
                pila.append(Nodo(int(simbolo)))
            else:
                nodo = Nodo(simbolo)
                nodo.derecha = pila.pop()
                nodo.izquierda = pila.pop()
                pila.append(nodo)
        return pila.pop()

    def recorrer_preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.recorrer_preorden(nodo.izquierda)
            self.recorrer_preorden(nodo.derecha)

    def recorrer_inorden(self, nodo):
        if nodo:
            self.recorrer_inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.recorrer_inorden(nodo.derecha)

    def recorrer_postorden(self, nodo):
        if nodo:
            self.recorrer_postorden(nodo.izquierda)
            self.recorrer_postorden(nodo.derecha)
            print(nodo.valor, end=' ')

    def evaluar(self, nodo):
        if isinstance(nodo.valor, int):
            return nodo.valor
        izquierda = self.evaluar(nodo.izquierda)
        derecha = self.evaluar(nodo.derecha)
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha

# Ejemplo de uso
expresion_postfija = "34+56+*"  # Representa (3 + 4) * (5 + 6)
arbol = ArbolExpresion(expresion_postfija)

print("Recorrido Preorden:")
arbol.recorrer_preorden(arbol.raiz)
print("\nRecorrido Inorden:")
arbol.recorrer_inorden(arbol.raiz)
print("\nRecorrido Postorden:")
arbol.recorrer_postorden(arbol.raiz)
print("\nEvaluación de la Expresión:", arbol.evaluar(arbol.raiz))
