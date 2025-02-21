INF = float('inf')  # Representa infinito (ausencia de conexión)

def floyd_warshall(graph):
    V = len(graph)
    
    # Inicializar matrices de distancias y predecesores
    dist = [row[:] for row in graph]  # Copia la matriz de adyacencia
    next_node = [[None if graph[i][j] == INF else j for j in range(V)] for i in range(V)]
    
    # Aplicar el algoritmo de Floyd-Warshall
    for k in range(V):  # Nodo intermedio
        for i in range(V):  # Nodo de inicio
            for j in range(V):  # Nodo destino
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]  # Guardar el nodo intermedio

    # Detección de ciclos negativos
    for i in range(V):
        if dist[i][i] < 0:
            print("¡El grafo tiene un ciclo negativo!")
            return None, None

    return dist, next_node

# Función para reconstruir el camino más corto entre dos nodos
def reconstruct_path(start, end, next_node):
    if next_node[start][end] is None:
        return []  # No hay camino
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path

# Definir el grafo como una matriz de adyacencia
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

# Ejecutar el algoritmo
dist_matrix, next_matrix = floyd_warshall(graph)

# Mostrar la matriz de distancias mínimas
if dist_matrix:
    print("\nMatriz de distancias mínimas:")
    for row in dist_matrix:
        print(row)

    # Mostrar caminos más cortos entre todos los pares de nodos
    print("\nRutas óptimas entre los nodos:")
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != j:
                path = reconstruct_path(i, j, next_matrix)
                if path:
                    print(f"Ruta más corta de {i} a {j}: {path} (Distancia: {dist_matrix[i][j]})")
                else:
                    print(f"No hay ruta de {i} a {j}")
