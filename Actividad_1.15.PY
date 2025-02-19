class GrafoMatriz:
    def __init__(self, vertices):
        self.V = vertices
        self.matriz = [[0] * vertices for _ in range(vertices)]

    def agregar_arista(self, u, v):
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1  # Para grafos no dirigidos

    def es_adyacente(self, u, v):
        return self.matriz[u][v] == 1
