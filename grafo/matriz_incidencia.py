from grafo.base import GrafoBase

class MatrizIncidencia(GrafoBase):
    def __init__(self, num_vertices):
        super().__init__(num_vertices)
        self.matriz = [] 

    def adicionar_aresta(self, u, v, peso=1):
        
        nova_coluna = [0] * self.num_vertices
        nova_coluna[u] = 1
        nova_coluna[v] = -1  # Ou 1 para grafos não direcionados
        self.matriz.append(nova_coluna)
        self.num_arestas += 1

    def remover_aresta(self, index):
        if 0 <= index < len(self.matriz):
            del self.matriz[index]
            self.num_arestas -= 1

    def mostrar(self):
        for coluna in zip(*self.matriz):
            print(coluna)
