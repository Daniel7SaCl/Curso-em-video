valores = tuple(int(input(f"Digite o {i+1}º valor: ")) for i in range(4))

quantidade_9 = valores.count(9)

posicoes_3 = [i for i, x in enumerate(valores) if x == 3]
primeira_posicao_3 = posicoes_3[0] if posicoes_3 else None

numeros_pares = [x for x in valores if x % 2 == 0]

print("A) Quantidade de vezes que o valor 9 apareceu:", quantidade_9)
print("B) Posição em que foi digitado o primeiro valor 3:", primeira_posicao_3)
print("C) Números pares digitados:", numeros_pares)
