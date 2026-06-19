import heapq

def algoritmo_prim(grafo, no_inicial):
    mst_rota = []  # Armazena as arestas da Árvore Geradora Mínima (Minimum Spanning Tree)
    visitados = set([no_inicial])
    
    # Inicializa o min-heap com as arestas saindo do nó inicial
    # Formato da tupla no heap: (peso, nó_origem, nó_destino)
    arestas = [
        (peso, no_inicial, destino)
        for destino, peso in grafo[no_inicial].items()
    ]
    heapq.heapify(arestas)
    
    custo_total = 0

    while arestas:
        peso, origem, destino = heapq.heappop(arestas)
        
        # Se o nó destino ainda não foi visitado, incluímos na nossa rede
        if destino not in visitados:
            visitados.add(destino)
            mst_rota.append((origem, destino, peso))
            custo_total += peso
            
            # Adiciona as novas arestas possíveis ao heap
            for proximo_destino, proximo_peso in grafo[destino].items():
                if proximo_destino not in visitados:
                    heapq.heappush(arestas, (proximo_peso, destino, proximo_destino))

    return mst_rota, custo_total

# Representação do grafo utilizando as distâncias fornecidas no texto
grafo = {
    'A': {'B': 4, 'C': 4},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 5, 'E': 6},
    'D': {'B': 5, 'C': 5, 'E': 3, 'F': 4},  # D-E = 3 conforme texto (imagem mostra 4)
    'E': {'C': 6, 'D': 3, 'F': 2},
    'F': {'D': 4, 'E': 2}
}

# Executando o algoritmo partindo do polo 'A'
rota_cabos, quilometros_totais = algoritmo_prim(grafo, 'A')

# Exibindo os resultados
print("=== Rota dos Cabos a Serem Instalados (Ordem de Construção) ===")
for origem, destino, peso in rota_cabos:
    print(f"Instalar cabo de {origem} para {destino}: {peso} Km")
    
print("-" * 50)
print(f"Quantidade total mínima de cabos utilizados: {quilometros_totais} Km")
