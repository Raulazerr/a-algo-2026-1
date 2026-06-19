import random
import time

def encontrar_subconjunto(numeros, alvo, indice=0, soma_atual=0, subconjunto_atual=None):
    if subconjunto_atual is None:
        subconjunto_atual = []

    # Condição de parada de sucesso: soma atingiu o alvo (e garantimos que o subconjunto não é vazio)
    if soma_atual == alvo and len(subconjunto_atual) > 0:
        return True, subconjunto_atual

    # Condição de parada de falha: testamos todos os números nesta ramificação e não deu o alvo
    if indice == len(numeros):
        return False, []

    # Ramificação 1: INCLUIR o número atual no subconjunto e continuar a busca
    encontrado, resultado = encontrar_subconjunto(
        numeros, 
        alvo, 
        indice + 1, 
        soma_atual + numeros[indice], 
        subconjunto_atual + [numeros[indice]]
    )
    if encontrado:
        return True, resultado

    # Ramificação 2: NÃO INCLUIR o número atual e continuar a busca
    encontrado, resultado = encontrar_subconjunto(
        numeros, 
        alvo, 
        indice + 1, 
        soma_atual, 
        subconjunto_atual
    )
    
    return encontrado, resultado

# ==========================================
# CASOS DE TESTE DO DEVER DE CASA
# ==========================================

# 1. Tamanho Pequeno (n = 4)
S_pequeno = [2, 4, 6, 10]
T_pequeno = 16
print("=== CASO 1: TAMANHO PEQUENO (n=4) ===")
sucesso, sub = encontrar_subconjunto(S_pequeno, T_pequeno)
print(f"Alvo {T_pequeno} encontrado no subconjunto: {sub}\n")

# 2. Tamanho Médio (n = 8)
S_medio = [-5, -2, 1, 3, 7, 12, 15, 21]
T_medio = 0
print("=== CASO 2: TAMANHO MÉDIO (n=8) ===")
sucesso, sub = encontrar_subconjunto(S_medio, T_medio)
print(f"Alvo {T_medio} encontrado no subconjunto: {sub}\n")

# 3. Tamanho Grande (n = 30)
# Gerando 30 números aleatórios de 5 dígitos (entre 10000 e 99999)
random.seed(42) # Semente fixa para o resultado ser sempre o mesmo ao rodar
S_grande = [random.randint(10000, 99999) for _ in range(30)]

# Vamos forçar que o alvo exista pegando 5 números aleatórios do nosso array e somando
subconjunto_secreto = random.sample(S_grande, 5)
T_grande = sum(subconjunto_secreto)

print("=== CASO 3: TAMANHO GRANDE (n=30) ===")
print(f"Procurando o alvo {T_grande} em um conjunto de 30 números...")
print(f"Conjunto: {S_grande[:5]}... (truncado)")

inicio_tempo = time.time()
sucesso, sub = encontrar_subconjunto(S_grande, T_grande)
fim_tempo = time.time()

if sucesso:
    print(f"SUCESSO! Alvo {T_grande} encontrado no subconjunto: {sub}")
else:
    print("Nenhum subconjunto encontrado para o alvo.")
    
print(f"Tempo levado para calcular: {fim_tempo - inicio_tempo:.4f} segundos")
