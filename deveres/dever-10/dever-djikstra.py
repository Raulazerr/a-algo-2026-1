def resolver_dever_dijkstra():
    # 1. Descrição do Problema (Grafo)
    # Dicionário onde a chave é o nó de origem e o valor é outro dicionário com {nó_destino: peso}
    grafo = {
        0: {1: 4, 2: 1},
        1: {3: 1},
        2: {1: 2, 4: 5},
        3: {4: 1},
        4: {}
    }
    
    inicio = 0
    destino = 4
    vertices = sorted(list(grafo.keys()))
    
    # Inicialização das distâncias e predecessores
    distancias = {v: float('inf') for v in vertices}
    distancias[inicio] = 0
    predecessores = {v: '-' for v in vertices}
    visitados = set()

    # Função auxiliar para imprimir uma linha formatada da tabela
    def imprimir_linha(passo, no_visitado):
        linha = f"| {passo:^5} | {no_visitado:^11} |"
        for v in vertices:
            dist = distancias[v] if distancias[v] != float('inf') else '∞'
            pred = predecessores[v]
            celula = f"{dist} ({pred})"
            linha += f" {celula:^7} |"
        print(linha)

    # Imprimir o cabeçalho da tabela
    print("=== EXECUÇÃO PASSO A PASSO ===")
    print("| Passo | Nó Visitado |  Nó 0   |  Nó 1   |  Nó 2   |  Nó 3   |  Nó 4   |")
    print("|:-----:|:-----------:|:-------:|:-------:|:-------:|:-------:|:-------:|")
    
    # Estado inicial (Passo 0)
    imprimir_linha(0, "N/A")

    passo = 1
    
    # 2. Execução do Algoritmo
    while len(visitados) < len(vertices):
        # Encontra o nó não visitado com a menor distância atual
        no_atual = None
        menor_distancia = float('inf')
        
        for v in vertices:
            if v not in visitados and distancias[v] < menor_distancia:
                menor_distancia = distancias[v]
                no_atual = v
                
        # Se não houver mais nós alcançáveis, encerra o loop
        if no_atual is None:
            break
            
        # Marca o nó como visitado
        visitados.add(no_atual)
        
        # Atualiza as distâncias dos vizinhos do nó atual
        for vizinho, peso in grafo[no_atual].items():
            if vizinho not in visitados:
                nova_distancia = distancias[no_atual] + peso
                
                # Se o novo caminho for mais curto, atualiza a distância e o predecessor
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = no_atual
                    
        # Imprime o estado da tabela após processar o nó atual
        imprimir_linha(passo, str(no_atual))
        passo += 1
        
        # Opcional: Se quisermos parar assim que o destino for visitado
        if no_atual == destino:
            break

    # 3. Reconstrução do Caminho Final
    caminho = []
    atual = destino
    
    # Rastreia de trás para frente usando os predecessores
    while atual != '-':
        caminho.insert(0, atual) # Insere sempre no início da lista
        atual = predecessores[atual]
        if atual == inicio:
            caminho.insert(0, atual)
            break

    # Imprimir os resultados finais
    print("\n=== RESULTADO FINAL ===")
    print(f"Caminho percorrido: {' ➔ '.join(map(str, caminho))}")
    print(f"Custo mínimo total: {distancias[destino]}")

# Executa o código
resolver_dever_dijkstra()
