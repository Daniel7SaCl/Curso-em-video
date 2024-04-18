import random

numeros_aleatorios = tuple(random.randint(1, 100) for _ in range(5))

print("Números gerados:", numeros_aleatorios)

menor_valor = min(numeros_aleatorios)
maior_valor = max(numeros_aleatorios)

print("Menor valor na tupla:", menor_valor)
print("Maior valor na tupla:", maior_valor)
