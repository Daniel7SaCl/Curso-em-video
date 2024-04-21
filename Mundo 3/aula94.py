jogadores = []

while True:
    jogador = {}

    jogador['nome'] = input("Digite o nome do jogador: ")

    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    gols_partidas = []
    for partida in range(1, jogador['partidas'] + 1):
        gols = int(input(f"Quantos gols {jogador['nome']} fez na partida {partida}? "))
        gols_partidas.append(gols)

    jogador['gols'] = gols_partidas

    jogadores.append(jogador)

    continuar = input("Deseja cadastrar outro jogador? (s/n): ")
    if continuar.lower() != 's':
        break

print("\nAproveitamento de cada jogador:")
for jogador in jogadores:
    print("\nNome:", jogador['nome'])
    print("Gols por partida:", jogador['gols'])
    total_gols = sum(jogador['gols'])
    print("Total de gols:", total_gols)
    print("Média de gols por partida:", total_gols / jogador['partidas'])
