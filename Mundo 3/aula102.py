def ficha(nome='<desconhecido>', gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

nome = input("Nome do jogador: ").strip()
gols = input("Número de gols: ").strip()

if gols.isnumeric():
    gols = int(gols)
    ficha(nome, gols)
else:
    ficha(nome)
