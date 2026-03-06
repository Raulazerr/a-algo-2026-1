import time
import random

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

tamanhos = [1000, 5000, 10000, 20000, 50000]

for n in tamanhos:

    lista = [random.randint(0, 100000) for i in range(n)]

    lista2 = lista.copy()

    inicio = time.time()
    insertion_sort(lista)
    fim = time.time()

    tempo_insertion = fim - inicio

    inicio = time.time()
    sorted(lista2)
    fim = time.time()

    tempo_sorted = fim - inicio

    print(f"\nTamanho da lista: {n}")
    print(f"Insertion Sort: {tempo_insertion:.6f} segundos")
    print(f"sorted() (Timsort): {tempo_sorted:.6f} segundos")
