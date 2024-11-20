def eh_vazio(grafo):
    return grafo.num_arestas == 0

def eh_completo(grafo):
    max_arestas = grafo.num_vertices * (grafo.num_vertices - 1) // 2
    return grafo.num_arestas == max_arestas
