import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = {}
    
    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1][nodo2] = peso
            self.grafo[nodo2][nodo1] = peso  # Grafo no dirigido
    
    def obtener_vecinos(self, nodo):
        return self.grafo.get(nodo, {})

    def heuristica(self, nodo, objetivo):
        return abs(hash(nodo) - hash(objetivo)) % 100  # Heurística simplificada

    def a_estrella(self, inicio, objetivo):
        frontera = []
        heapq.heappush(frontera, (0, inicio))
        came_from = {inicio: None}
        costo_acumulado = {inicio: 0}
        
        while frontera:
            costo_actual, nodo_actual = heapq.heappop(frontera)
            
            if nodo_actual == objetivo:
                break
            
            for vecino, costo in self.obtener_vecinos(nodo_actual).items():
                nuevo_costo = costo_acumulado[nodo_actual] + costo
                if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                    costo_acumulado[vecino] = nuevo_costo
                    prioridad = nuevo_costo + self.heuristica(vecino, objetivo)
                    heapq.heappush(frontera, (prioridad, vecino))
                    came_from[vecino] = nodo_actual
        
        return self.reconstruir_camino(came_from, inicio, objetivo)
    
    def reconstruir_camino(self, came_from, inicio, objetivo):
        camino = []
        nodo = objetivo
        while nodo:
            camino.append(nodo)
            nodo = came_from[nodo]
        return camino[::-1]

    def visualizar_grafo(self):
        G = nx.Graph()
        for nodo, vecinos in self.grafo.items():
            for vecino, peso in vecinos.items():
                G.add_edge(nodo, vecino, weight=peso)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

# Ejemplo de uso
grafo = Grafo()
nodos = ['A', 'B', 'C', 'D', 'E']
for nodo in nodos:
    grafo.agregar_nodo(nodo)

grafo.agregar_arista('A', 'B', 4)
grafo.agregar_arista('A', 'C', 2)
grafo.agregar_arista('B', 'C', 5)
grafo.agregar_arista('B', 'D', 10)
grafo.agregar_arista('C', 'D', 3)
grafo.agregar_arista('D', 'E', 7)

grafo.visualizar_grafo()
camino_optimo = grafo.a_estrella('A', 'E')
print("Camino óptimo:", camino_optimo)
