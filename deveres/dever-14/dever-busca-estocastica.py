import random
import math
import matplotlib.pyplot as plt

# SIMULAÇÃO DO 'nqueens_utils.py' (Para o código rodar sozinho)

def calcular_ataques(estado):
    """Calcula quantos pares de rainhas estão se atacando (apenas diagonais importam aqui)."""
    ataques = 0
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(estado[i] - estado[j]) == abs(i - j):
                ataques += 1
    return ataques

def gerar_vizinho(estado):
    """Gera um vizinho trocando a posição de duas rainhas."""
    vizinho = list(estado)
    i, j = random.sample(range(len(estado)), 2)
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
    return vizinho

# SEU DEVER DE CASA: LOOP DO SIMULATED ANNEALING

def simulated_annealing(n=12, temp_inicial=100.0, taxa_resfriamento=0.95, max_iter=2000):
    # Estado inicial: uma rainha por coluna, linhas embaralhadas
    estado_atual = list(range(n))
    random.shuffle(estado_atual)
    
    custo_atual = calcular_ataques(estado_atual)
    temp = temp_inicial
    historico_custos = [custo_atual]
    
    for _ in range(max_iter):
        # Se encontrou a solução perfeita (0 ataques), pode parar
        if custo_atual == 0:
            break 
            
        vizinho = gerar_vizinho(estado_atual)
        custo_vizinho = calcular_ataques(vizinho)
        
        delta_e = custo_vizinho - custo_atual
        
        # Aceitação: se for melhor (delta_e < 0) ou pela probabilidade de Boltzmann
        if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
            estado_atual = vizinho
            custo_atual = custo_vizinho
            
        historico_custos.append(custo_atual)
        temp *= taxa_resfriamento # Resfria a temperatura
        
    return estado_atual, custo_atual, historico_custos


# COMPARAÇÃO E GERAÇÃO DO GRÁFICO

# Executa o SA
estado_final, custo_final, historico_sa = simulated_annealing(n=12)

# Criando uma curva fictícia de AG para fins de comparação no gráfico
# (Você pode substituir isso pelos dados reais do log do seu AG, se tiver)
historico_ag = [historico_sa[0]]
for _ in range(len(historico_sa) - 1):
    # Simulando uma convergência mais lenta e em "degraus" típica do AG
    novo_custo = max(0, historico_ag[-1] - random.uniform(0, 0.4))
    historico_ag.append(novo_custo)

# Plotando o Gráfico
plt.figure(figsize=(10, 5))
plt.plot(historico_sa, label='Simulated Annealing (SA)', color='#e74c3c', linewidth=2)
plt.plot(historico_ag, label='Algoritmo Genético (AG) - Simulado', color='#3498db', linestyle='--')
plt.title('Convergência nas 12-Rainhas: SA vs AG')
plt.xlabel('Iterações / Avaliações')
plt.ylabel('Custo (Número de Ataques)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print(f"Custo Final do SA: {custo_final} ataques.")
