import random

numero_secreto = random.randint(0, 10)

palpites = 0

while True:
    palpite = int(input("Digite seu palpite (entre 0 e 10): "))

    palpites += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número em", palpites, "palpites!")
        break
    else:
        if palpite < numero_secreto:
            print("Tente um número mais alto.")
        else:
            print("Tente um número mais baixo.")
