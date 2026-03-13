import sys, time

sys.setrecursionlimit(1500)

# Fatorial usando condicional ternária
def fat(n):
    return 1 if n <= 1 else n * fat(n - 1)

# Valores para um resultado
for n in [10, 100, 500, 1000]:
    t0 = time.perf_counter()
    _ = fat(n)
    t1 = time.perf_counter()
    print(f"Entrada {n} demorou {t1 - t0:.10f} segundos.")

# Tempos de execução: 
# Entrada 10 demorou 0.0000020000 segundos.
# Entrada 100 demorou 0.0000122003 segundos. 
# Entrada 500 demorou 0.0000996003 segundos. 
# Entrada 1000 demorou 0.0002925000 segundos.

# Cada chamada executa apenas operações constantes. Assim, o tempo cresce proporcionalmente ao número de chamadas.
# T(n) = O(n)
