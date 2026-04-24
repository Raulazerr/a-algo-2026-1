def eh_palindromo(arr, inicio, fim):
    # Caso base: quando os índices se cruzam ou são iguais
    if inicio >= fim:
        return True
    
    # Se os elementos forem diferentes, não é palíndromo
    if arr[inicio] != arr[fim]:
        return False
    
    # Chamada recursiva avançando para o centro
    return eh_palindromo(arr, inicio + 1, fim - 1)


# Entrada do usuário (ex: 1 2 3 2 1)
entrada = input("Digite os elementos do array separados por espaço: ")
array = entrada.split()

# Verificação
if eh_palindromo(array, 0, len(array) - 1):
    print("É palíndromo")
else:
    print("Não é palíndromo")
