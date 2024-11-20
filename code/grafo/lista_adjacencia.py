from grafo.base import GrafoBase

class ListaAdjacencia(GrafoBase):
    def __init__(self, num_vertices):
        super().__init__(num_vertices)
        self.lista = [[] for _ in range(num_vertices)]  

    def adicionar_aresta(self, u, v, peso=1):
        self.lista[u].append((v, peso))
        self.lista[v].append((u, peso))  # Apenas para grafos não direcionados
        self.num_arestas += 1

    def remover_aresta(self, u, v):
        self.lista[u] = [(x, p) for x, p in self.lista[u] if x != v]
        self.lista[v] = [(x, p) for x, p in self.lista[v] if x != u]
        self.num_arestas -= 1

    def mostrar(self):
        for i, vizinhos in enumerate(self.lista):
            print(f"{i}: {vizinhos}")
