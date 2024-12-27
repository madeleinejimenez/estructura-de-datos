# Implementación de la pila utilizando listas enlazadas

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaListaEnlazada:
    def __init__(self):
        self.cima = None

    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.cima.dato

    def is_empty(self):
        return self.cima is None

# Implementación de la pila utilizando arreglos

class PilaArreglo:
    def __init__(self):
        self.elementos = []

    def push(self, dato):
        self.elementos.append(dato)

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.elementos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.elementos[-1]

    def is_empty(self):
        return len(self.elementos) == 0

# Evaluación de expresiones aritméticas en notación posfija

def evaluar_expresion_posfija(expresion, pila):
    for token in expresion.split():
        if token.isdigit():
            pila.push(int(token))
        elif token in ['+', '-', '*', '/']:
            if pila.is_empty():
                raise ValueError("Expresión inválida: falta operando")
            operando2 = pila.pop()
            if pila.is_empty():
                raise ValueError("Expresión inválida: falta operando")
            operando1 = pila.pop()

            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                if operando2 == 0:
                    raise ZeroDivisionError("División entre cero")
                resultado = operando1 / operando2

            pila.push(resultado)
        else:
            raise ValueError(f"Token inválido: {token}")

    if pila.is_empty() or len(pila.elementos if isinstance(pila, PilaArreglo) else [nodo for nodo in iter(lambda: pila.cima, None)]) != 1:
        raise ValueError("Expresión inválida")

    return pila.pop()

# Ejemplo de uso
if __name__ == "__main__":
    # Cambiar entre PilaListaEnlazada y PilaArreglo según se desee
    pila = PilaArreglo()
    # pila = PilaListaEnlazada()

    expresion = "3 4 + 2 * 7 /"  # Ejemplo: ((3 + 4) * 2) / 7
    resultado = evaluar_expresion_posfija(expresion, pila)
    print(f"El resultado de la expresión '{expresion}' es: {resultado}")
