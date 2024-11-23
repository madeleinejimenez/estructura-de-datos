# main.py
from pila import Pila

def evaluar_postfija(expresion):
    """Evalúa una expresión postfija usando una pila"""
    pila = Pila()
    for elemento in expresion.split():
        if elemento.isdigit():
            pila.push(int(elemento))
        else:
            b = pila.pop()
            a = pila.pop()
            if elemento == '+':
                pila.push(a + b)
            elif elemento == '-':
                pila.push(a - b)
            elif elemento == '*':
                pila.push(a * b)
            elif elemento == '/':
                pila.push(a / b)
    return pila.pop()

def main():
    print("Bienvenido al evaluador de expresiones postfijas.")
    while True:
        expresion = input("Ingrese una expresión postfija (o 'salir' para terminar): ")
        if expresion.lower() == 'salir':
            print("¡Hasta luego!")
            break
        try:
            resultado = evaluar_postfija(expresion)
            print(f"El resultado es: {resultado}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
