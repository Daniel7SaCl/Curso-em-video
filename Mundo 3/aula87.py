import random

def gerar_palpite():
    return sorted(random.sample(range(1, 61), 6))

num_jogos = int(input("Quantos jogos deseja gerar? "))

jogos = []
for _ in range(num_jogos):
    palpite = gerar_palpite()
    jogos.append(palpite)

print("\nPalpites gerados:")
for i, palpite in enumerate(jogos, start=1):
    print(f"Jogo {i}: {palpite}")
