import random

print("Bem-vindo ao Jokenpô!")
while True:
    player = input("Escolha pedra, papel ou tesoura (ou 'sair' para sair): ").lower()
    if player == 'sair':
        print("Obrigado por jogar!")
        break
    elif player != 'pedra' and player != 'papel' and player != 'tesoura':
        print("Escolha inválida. Tente novamente.")
        continue

    computer = random.choice(['pedra', 'papel', 'tesoura'])
    print("Você escolheu: {}".format(player))
    print("O computador escolheu: {}".format(computer))

    if player == computer:
        print("Empate!")
    elif (player == 'pedra' and computer == 'tesoura') or \
         (player == 'papel' and computer == 'pedra') or \
         (player == 'tesoura' and computer == 'papel'):
        print("Você ganhou!")
    else:
        print("Computador ganhou!")