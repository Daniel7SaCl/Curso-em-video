import random

def sorteia():
    numeros = []
    for _ in range(5):
        numeros.append(random.randint(1, 10))
    print("Números sorteados:", numeros)
    return numeros

def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print("Soma dos números pares:", soma)

numeros_sorteados = sorteia()
somaPar(numeros_sorteados)
