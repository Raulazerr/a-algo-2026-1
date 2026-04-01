import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    
    return merge(esquerda, direita)

def merge(esq, dir):
    resultado = []
    i = j = 0
    
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    
    return resultado

def multiplicacao_matrizes(A, B):
    n = len(A)
    
    # matriz resultado
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C

import math

def T1(n):
    if n <= 1:
        return 1
    return 2 * T1(n // 4) + math.sqrt(n)

def T2(n):
    if n <= 1:
        return 1
    return 2 * T2(n // 4) + n

def T3(n):
    if n <= 1:
        return 1
    return 16 * T3(n // 4) + n**2

#Teste T3(n)
print("T3(1024):", T3(1024))

#Teste T2(n)
print("T2(1024):", T2(1024))

#Teste T1(n)
print("T1(1024):", T1(1024))

# Teste multiplicação de matrizes
n = 100
A = [[1 for _ in range(n)] for _ in range(n)]
B = [[1 for _ in range(n)] for _ in range(n)]

inicio = time.perf_counter()
multiplicacao_matrizes(A, B)
fim = time.perf_counter()

print(f"Multiplicação de matrizes {n}x{n}: {fim - inicio:.6f} segundos")

# Teste de desempenho do merge sort
n = 10000
lista = [random.randint(0, 10000) for _ in range(n)]

inicio = time.perf_counter()
merge_sort(lista)
fim = time.perf_counter()

print(f"Merge Sort com n={n}: {fim - inicio:.6f} segundos")
