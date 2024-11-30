import time
import random

# Código original
def calcular_suma(lista):
    suma = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            suma += lista[i] * lista[j]
    return suma

# Código optimizado
def calcular_suma_opt(lista):
    suma = 0
    suma_elementos = sum(lista)  # Calcula la suma total de los elementos
    for i in lista:
        suma += i * suma_elementos  # Suma el producto de cada elemento por la suma total
    return suma

# Generamos listas de tamaño 100, 1000, 10000
sizes = [100, 1000, 10000]
times_original = []
times_optimized = []

for size in sizes:
    lista = [random.randint(1, 100) for _ in range(size)]
    
    # Medimos el tiempo del código original
    start = time.time()
    calcular_suma(lista)
    end = time.time()
    times_original.append(end - start)
    
    # Medimos el tiempo del código optimizado
    start = time.time()
    calcular_suma_opt(lista)
    end = time.time()
    times_optimized.append(end - start)
    
print("Tiempos de ejecución (segundos):")
print(f"Tamaño de lista: {sizes}")
print(f"Original: {times_original}")
print(f"Optimizado: {times_optimized}")
