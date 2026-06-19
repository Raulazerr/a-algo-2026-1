def dever_bellman_ford():
    # Definição dos vértices e da origem
    vertices = [0, 1, 2, 3, 4]
    origem = 0
    
    # Definição das arestas no formato (origem, destino, peso)
    arestas = [
        (0, 1, 5),
        (1, 2, 1),
        (1, 3, 2),
        (2, 4, 1),
        (4, 3, -1)
    ]
    
    # Inicialização
    # Distâncias começam no infinito para todos, exceto a origem (0)
    distancias = {v: float('inf') for v in vertices}
    distancias[origem] = 0
    
    # Predecessores começam vazios
    predecessores = {v: '-' for v in vertices}
    
    # Função auxiliar para imprimir uma linha da tabela formatada
    def imprimir_linha(nome_iteracao):
        linha = f"{nome_iteracao:<10} |"
        for v in vertices:
            dist = distancias[v] if distancias[v] != float('inf') else '∞'
            pred = predecessores[v]
            celula = f"{dist} ({pred})"
            linha += f" {celula:^9} |"
        print(linha)

    # Imprimir o cabeçalho da tabela
    print("-" * 71)
    print("Iteração   | Vértice 0 | Vértice 1 | Vértice 2 | Vértice 3 | Vértice 4 |")
    print("-" * 71)
    
    # Estado inicial
    imprimir_linha("Inicial")
    
    # Relaxamento das arestas (O algoritmo roda |V| - 1 vezes)
    num_iteracoes = len(vertices) - 1
    
    for i in range(1, num_iteracoes + 1):
        # Usamos uma cópia das distâncias da iteração anterior para garantir 
        # que o passo a passo corresponda exatamente ao avanço de 1 aresta por vez
        distancias_anteriores = distancias.copy()
        houve_mudanca = False
        
        for u, v, peso in arestas:
            # Se o nó de origem já foi alcançado e o novo caminho é mais curto
            if distancias_anteriores[u] != float('inf') and distancias_anteriores[u] + peso < distancias[v]:
                distancias[v] = distancias_anteriores[u] + peso
                predecessores[v] = u
                houve_mudanca = True
                
        imprimir_linha(f"Iteração {i}")
        
        # Se não houve nenhuma mudança nesta iteração, podemos parar cedo (otimização)
        # Comentado para forçar a impressão de todas as iterações da tabela
        # if not houve_mudanca:
        #     break

    print("-" * 71)

    # Passo Final: Verificação de Ciclo Negativo
    # Se ainda for possível relaxar alguma aresta após |V| - 1 iterações, há um ciclo negativo
    tem_ciclo_negativo = False
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            tem_ciclo_negativo = True
            break
            
    print("\n--- RESULTADO DA VERIFICAÇÃO ---")
    if tem_ciclo_negativo:
        print("CONCLUSÃO: Existe um ciclo negativo no grafo!")
    else:
        print("CONCLUSÃO: Não existe ciclo negativo no grafo.")

# Executa o código
dever_bellman_ford()
