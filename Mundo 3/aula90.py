import random

resultados = {}

for jogador in range(1, 5):
    resultado = random.randint(1, 6)
    resultados[f"Jogador {jogador}"] = resultado

resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

print("Resultados dos jogadores:")
for jogador, resultado in resultados_ordenados.items():
    print(f"{jogador}: {resultado}")

vencedor = next(iter(resultados_ordenados))
print(f"\nO vencedor é {vencedor} com o resultado {resultados_ordenados[vencedor]}.")
