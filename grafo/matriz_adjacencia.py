from grafo.base import GrafoBase

class MatrizAdjacencia(GrafoBase):
    def __init__(self, num_vertices):
        super().__init__(num_vertices)
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v, peso=1):
        self.matriz[u][v] = peso
        self.matriz[v][u] = peso
        self.num_arestas += 1