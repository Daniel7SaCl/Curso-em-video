import random

vitorias_consecutivas = 0

while True:
    
    escolha_j = input("Escolha par (p) ou ímpar (i): ").lower()
    while escolha_j not in ['p', 'i']:
        escolha_j = input("Escolha inválida. Escolha par (p) ou ímpar (i): ").lower()

    numero_computador = random.randint(1, 10)
    print("O computador escolheu o número:", numero_computador)

    numero_jogador = int(input("Escolha um número entre 1 e 10: "))

    soma = numero_jogador + numero_computador
    print("A soma dos números é:", soma)

    if soma % 2 == 0:
        resultado = 'p'
    else:
        resultado = 'i'

    if resultado == escolha_j:
        print("Você ganhou!")
        vitorias_consecutivas += 1
        print("Vitórias consecutivas:", vitorias_consecutivas)
    else:
        print("Você perdeu!")
        print("Total de vitórias consecutivas:", vitorias_consecutivas)
        break
