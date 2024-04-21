nome_jogador = input("Digite o nome do jogador: ")

quantidade_partidas = int(input(f"Quantas partidas {nome_jogador} jogou? "))

aproveitamento = {'nome': nome_jogador, 'gols': [], 'total_de_gols': 0}

for partida in range(1, quantidade_partidas + 1):
    gols_partida = int(input(f"Quantos gols {nome_jogador} fez na partida {partida}? "))
    aproveitamento['gols'].append(gols_partida)
    aproveitamento['total_de_gols'] += gols_partida

print("\nAproveitamento do jogador:")
print(f"Nome: {aproveitamento['nome']}")
print("Gols por partida:", aproveitamento['gols'])
print(f"Total de gols no campeonato: {aproveitamento['total_de_gols']}")
