# Búsqueda de elemento mayor y menor
def buscar_mayor(arr):
    """Encuentra el mayor elemento en un arreglo."""
    if not arr:
        raise ValueError("El arreglo está vacío")
    mayor = arr[0]
    for num in arr:
        if num > mayor:
            mayor = num
    return mayor

def buscar_menor(arr):
    """Encuentra el menor elemento en un arreglo."""
    if not arr:
        raise ValueError("El arreglo está vacío")
    menor = arr[0]
    for num in arr:
        if num < menor:
            menor = num
    return menor
# Bubble Sort
def bubble_sort(arr):
    """Ordena un arreglo usando el algoritmo Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Selection Sort
def selection_sort(arr):
    """Ordena un arreglo usando el algoritmo Selection Sort."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
def main():
    print("Bienvenido al programa de algoritmos con arreglos.")
    arreglo = [64, 34, 25, 12, 22, 11, 90]
    print(f"Arreglo original: {arreglo}")

    # Búsqueda
    mayor = buscar_mayor(arreglo)
    menor = buscar_menor(arreglo)
    print(f"Elemento mayor: {mayor}")
    print(f"Elemento menor: {menor}")

    # Ordenación
    bubble_sorted = arreglo[:]
    bubble_sort(bubble_sorted)
    print(f"Arreglo ordenado con Bubble Sort: {bubble_sorted}")

    selection_sorted = arreglo[:]
    selection_sort(selection_sorted)
    print(f"Arreglo ordenado con Selection Sort: {selection_sorted}")

if __name__ == "__main__":
    main()

