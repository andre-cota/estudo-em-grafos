class GrafoBase:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_arestas = 0

    def adicionar_aresta(self, u, v, peso=1):
        raise NotImplementedError

    def remover_aresta(self, u, v):
        raise NotImplementedError

    def mostrar(self):
        raise NotImplementedError