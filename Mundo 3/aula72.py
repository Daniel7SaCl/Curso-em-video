primeiros_colocados = (
    "Flamengo", "Palmeiras", "Atlético Mineiro", "Fortaleza", "Corinthians",
    "Internacional", "Athletico Paranaense", "Fluminense", "Cuiabá", "Santos",
    "Atlético Goianiense", "Bahia", "Juventude", "São Paulo", "Sport Recife",
    "América Mineiro", "Ceará", "Grêmio", "Internacional", "Chapecoense"
)
# a) Os 5 primeiros times
print("a) Os 5 primeiros times:")
print(primeiros_colocados[:5])

print("\nb) Os últimos 4 colocados:")
print(primeiros_colocados[-4:])

print("\nc) Times em ordem alfabética:")
print(sorted(primeiros_colocados))

posicao_chapecoense = primeiros_colocados.index("Chapecoense") + 1
print("\nd) Em que posição está o time da Chapecoense:")
print("Chapecoense está na posição:", posicao_chapecoense)
